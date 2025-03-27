# -*- coding: utf-8 -*-
# from collective.volto.sitesettings.testing import COLLECTIVE_VOLTO_SITESETTINGS_FUNCTIONAL_TESTING
from collective.volto.sitesettings.testing import (
    COLLECTIVE_VOLTO_SITESETTINGS_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class UpgradeStepIntegrationTest(unittest.TestCase):
    layer = COLLECTIVE_VOLTO_SITESETTINGS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_upgrade_step(self):
        # dummy, add tests here
        self.assertTrue(True)


# class UpgradeStepFunctionalTest(unittest.TestCase):
#
#     layer = COLLECTIVE_VOLTO_SITESETTINGS_FUNCTIONAL_TESTING
#
#     def setUp(self):
#         self.portal = self.layer['portal']
#         setRoles(self.portal, TEST_USER_ID, ['Manager'])
