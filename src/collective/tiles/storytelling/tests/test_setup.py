# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.tiles.storytelling.testing import COLLECTIVE_ORGANIZATION_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.tiles.storytelling is properly installed."""

    layer = COLLECTIVE_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.tiles.storytelling is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.tiles.storytelling'))

    def test_browserlayer(self):
        """Test that ICollectiveTilesStorytellingLayer is registered."""
        from collective.tiles.storytelling.interfaces import (
            ICollectiveTilesStorytellingLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveTilesStorytellingLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.tiles.storytelling'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.tiles.storytelling is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.tiles.storytelling'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTilesStorytellingLayer is removed."""
        from collective.tiles.storytelling.interfaces import \
            ICollectiveTilesStorytellingLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveTilesStorytellingLayer,
            utils.registered_layers())
