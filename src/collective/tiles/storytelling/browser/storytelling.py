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


TEMPLATE = "<div class='side-text-slide'></div>"

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
            content = u'<p>This is a side text slide</p>'
        return u"<html><body>%s</body></html>" % safe_unicode(content)
