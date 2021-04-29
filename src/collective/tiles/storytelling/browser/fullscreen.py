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

from bs4 import BeautifulSoup as BSHTML
import re

class FullscreenSlideTile(Tile):
    template = ViewPageTemplateFile('templates/fullscreen.pt')

    def __call__(self):
        self.update()
        return self.template()

    def get_img_src(self, data):
        if data:
            soup = BSHTML(data)
            images = soup.findAll('img')
            if images:
                image = images[0]
                src = image['src']
                return src
            return ''
        else:
            return None

    def update(self):
        self.title = self.data.get('title', '')
        self.body = self.data.get('body', '')
        self.selected_image = self.data.get('selected_image', '')
        self.image_url = self.get_img_src(getattr(self.selected_image, 'output', None))
        self.tile_id = getUtility(IIDNormalizer).normalize(self.title)
        

class IFullscreenSlideTile(Schema):
    title = schema.TextLine(
        title=_(u"Slide title"),
        required=False,
    )
    
    body = RichText(
        title=_(u"Slide body text"),
        description=_(u"Text that appears on top of the fullscreen image"),
        required=True,
    )

    selected_image = RichText(
        title=_(u"Select an image"),
        description=_(u"Select or upload an image below"),
        required=True,
    )


