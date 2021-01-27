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

class TextSlideTile(Tile):
    template = ViewPageTemplateFile('templates/textslide.pt')

    def __call__(self):
        self.update()
        return self.template()

    def update(self):
        self.body = self.data.get('body', '')

class ITextSlideTile(Schema):
    body = RichText(
        title=_(u"Text slide body text"),
        description=_(u"Text that appears at the center of the slide"),
        required=True,
    )


