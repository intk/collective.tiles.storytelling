# -*- coding: utf-8 -*-
from plone.app.standardtiles import _PMF as _
from plone.subrequest import ISubRequest
from plone.supermodel.directives import primary
from plone.supermodel.model import Schema
from plone.tiles import Tile
from plone.tiles.directives import ignore_querystring
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope import schema
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone import api

class ISideTextTile(Schema):

    ignore_querystring('content')
    primary('content')
    content = schema.Text(
        title=_(u'HTML'),
        required=True,
    )

class SideTextTile(Tile):
    """
    A persistent HTML content tile that can be used for
    re-usable layouts in the mosaic editor
    """

    def __call__(self):
        content = self.data.get('content')
        if content:
            # only transform is not rendering for layout editor
            if (not self.request.get('_layouteditor') or
                    ISubRequest.providedBy(self.request)):
                transforms = getToolByName(self.context, 'portal_transforms')
                data = transforms.convertTo(
                    'text/x-html-safe',
                    safe_unicode(content), mimetype='text/html',
                    context=self.context
                )
                content = data.getData()
        else:
            content = u'<p>This is a side text slide - Default text</p>'
        return u"<html><body>%s</body></html>" % safe_unicode(content)

class SideTextSlideTile(Tile):
    template = ViewPageTemplateFile('templates/sidetext.pt')

    def __call__(self):
        self.update()
        return self.template()

    def update(self):
        self.title = self.data.get('title', '')
        self.body = self.data.get('body', '')
        self.alignment = self.data.get('image_alignment', '')
        self.tile_id = getUtility(IIDNormalizer).normalize(self.title)
        img_uid = self.data.get('image', None)
        
        if img_uid is None:
            self.image_url = None
        else:
            self.image_url = api.content.get(UID=img_uid).absolute_url()

class ISideTextSlideTile(Schema):
    title = schema.TextLine(
        title=_(u"Slide title"),
        required=True,
    )
    body = RichText(
        title=_(u"Slide body text"),
        description=_(u"Text that appears on the side of the slide"),
        required=True,
    )
    image = schema.Choice(
        title=_(u"Select an image"),
        required=True,
        vocabulary='plone.app.vocabularies.Catalog',
    )
    form.widget(
        'image',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            'recentlyUsed': True,
            'selectableTypes': ['Image'],
        }
    )

    image_alignment = schema.Choice(
        title=_(u"Choose image alignment"),
        description=_(u"Image is aligned to the left by default"),
        values=[_(u'Left'), _(u'Right')],
        default=_(u'Left'),
        required=False
    )


