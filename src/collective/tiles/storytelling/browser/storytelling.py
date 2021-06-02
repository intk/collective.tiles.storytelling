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

class SideTextSlideTile(Tile):
    template = ViewPageTemplateFile('templates/sidetext.pt')

    def __call__(self):
        self.update()
        return self.template()

    def update(self):
        self.title = self.data.get('title', '')
        self.body = self.data.get('body', '')
        self.alignment = self.data.get('image_alignment', '')
        self.selected_image = self.data.get('selected_image', '')
        self.image_caption = self.data.get('image_caption', '')
        self.tile_id = getUtility(IIDNormalizer).normalize(self.title)


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

    selected_image = RichText(
        title=_(u"Select an image"),
        description=_(u"Select or upload an image below"),
        required=True,
    )

    image_alignment = schema.Choice(
        title=_(u"Choose image alignment"),
        description=_(u"Image is aligned to the left by default"),
        values=[_(u'Left'), _(u'Right')],
        default=_(u'Left'),
        required=False
    )

    image_caption = schema.TextLine(
        title=_(u"Image caption / copyrights"),
        required=False,
    )


class VideoSlideTile(Tile):
    template = ViewPageTemplateFile('templates/videoslide.pt')

    def __call__(self):
        self.update()
        return self.template()

    def update(self):
        self.title = self.data.get('title', '')
        self.body = self.data.get('body', '')
        self.alignment = self.data.get('text_alignment', '')
        self.video_url = self.data.get('video_url', '')
        self.selected_image = self.data.get('selected_image', '')
        self.tile_id = getUtility(IIDNormalizer).normalize(self.title)


class IVideoSlideTile(Schema):
    title = schema.TextLine(
        title=_(u"Slide title"),
        required=True,
    )

    video_url = schema.TextLine(
        title=_(u"Youtube url"),
        required=True,
    )

    body = RichText(
        title=_(u"Slide body text"),
        description=_(u"Text that appears underneath the video"),
        required=True,
    )

    selected_image = RichText(
        title=_(u"Select an image for the video thumbnail"),
        description=_(u"This image will appear before the video starts playing"),
        required=True,
    )

    text_alignment = schema.Choice(
        title=_(u"Choose text alignment"),
        description=_(u"Text is aligned to the left by default"),
        values=[_(u'Left'), _(u'Right')],
        default=_(u'Left'),
        required=False
    )
