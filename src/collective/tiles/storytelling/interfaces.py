# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class ICollectiveTilesStorytellingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
