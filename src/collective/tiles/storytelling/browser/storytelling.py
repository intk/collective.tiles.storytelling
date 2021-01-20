# -*- coding: utf-8 -*-
from operator import itemgetter
from plone.app.contenttypes.behaviors.collection import ISyndicatableCollection
from plone.app.standardtiles import PloneMessageFactory as _
from plone.app.z3cform.widget import QueryStringFieldWidget
from plone.autoform.directives import widget
from plone.registry.interfaces import IRegistry
from plone.supermodel.model import Schema
from plone.tiles import Tile, PersistentTile
from plone.tiles.interfaces import ITileType
from Products.CMFCore.interfaces import IFolderish
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.interfaces import IValue
from z3c.form.util import getSpecification
from zope import schema
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider
from zope.schema import getFields
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary



