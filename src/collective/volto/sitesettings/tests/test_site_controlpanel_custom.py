from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsAdditionalSiteSchema,
)
from collective.volto.sitesettings.testing import RESTAPI_TESTING
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from plone.restapi.testing import RelativeSession
from transaction import commit
from zope.component import getUtility


try:
    from plone.base.interfaces.controlpanel import ISiteSchema
except ImportError:
    # Plone 52
    from Products.CMFPlone.interfaces import ISiteSchema

import base64
import os
import unittest


class SiteSettingsTest(unittest.TestCase):
    layer = RESTAPI_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()

        self.api_session = RelativeSession(self.portal_url)
        self.api_session.headers.update({"Accept": "application/json"})
        self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)

        registry = getUtility(IRegistry)
        self.site_proxy = registry.forInterface(ISiteSchema, prefix="plone")
        self.site_proxy_additional = registry.forInterface(
            ICollectiveVoltoSitesettingsAdditionalSiteSchema, prefix="plone"
        )

        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_controlpanel_return_additional_fields(self):
        response = self.api_session.get("/@controlpanels/site")

        result = response.json()
        fields = ["site_title_translated", "site_subtitle", "site_logo_footer"]

        for field in fields:
            self.assertIn(field, result["schema"]["properties"].keys())

    def test_saving_controlpanel_save_registry_data(self):
        self.assertEqual("Plone site", self.site_proxy.site_title)
        self.assertEqual("{}", self.site_proxy_additional.site_subtitle)
        self.assertEqual(
            '{"en": "Plone site"}', self.site_proxy_additional.site_title_translated
        )

        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_title_translated": '{"en": "Localized title"}',
                "site_subtitle": '{"en": "xxx"}',
            },
        )
        commit()

        # site_title is in sync with translated one
        self.assertEqual("Localized title", self.site_proxy.site_title)
        self.assertEqual(
            '{"en": "Localized title"}',
            self.site_proxy_additional.site_title_translated,
        )
        self.assertEqual('{"en": "xxx"}', self.site_proxy_additional.site_subtitle)

    def test_endpoint_return_site_title_based_on_language_if_set(self):
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_title": "Site custom name",
            },
        )
        commit()
        resp = self.api_session.get("/@site").json()
        self.assertEqual(resp["plone.site_title"], {"en": "Plone site"})

        # now try to add some localizations
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_title_translated": '{"en": "Localized title"}',
                "site_title": "Site custom name",
            },
        )
        commit()

        resp = self.api_session.get("/@site").json()
        self.assertEqual(
            resp["plone.site_title"],
            {"en": "Localized title"},
        )

    def test_endpoint_return_site_subtitle_based_on_language_if_set(self):
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_subtitle": '{"en": "Site subtitle"}',
            },
        )
        commit()
        resp = self.api_session.get("/@site").json()
        self.assertEqual(resp["plone.site_subtitle"], {"en": "Site subtitle"})

    def test_endpoint_store_logo_dimensions_if_saved(self):
        image_file = os.path.join(os.path.dirname(__file__), "logo.png")
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read())
        filename = base64.b64encode(b"logo.png")
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_logo": f"filenameb64:{filename.decode()};datab64:{image_data.decode()}",
            },
        )
        commit()

        self.assertEqual(441, self.site_proxy_additional.site_logo_width)
        self.assertEqual(114, self.site_proxy_additional.site_logo_height)

        resp = self.api_session.get("/@site").json()
        self.assertEqual(
            resp["plone.site_logo"],
            {
                "url": f"{self.portal_url}/registry-images/@@images/site_logo/logo.png",
                "width": 441,
                "height": 114,
            },
        )

    def test_endpoint_store_favicon_dimensions_if_saved(self):
        image_file = os.path.join(os.path.dirname(__file__), "favicon.ico")
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read())
        filename = base64.b64encode(b"favicon.ico")
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_favicon": f"filenameb64:{filename.decode()};datab64:{image_data.decode()}",
            },
        )
        commit()

        self.assertEqual(72, self.site_proxy_additional.site_favicon_width)
        self.assertEqual(72, self.site_proxy_additional.site_favicon_height)

        resp = self.api_session.get("/@site").json()
        self.assertEqual(
            resp["plone.site_favicon"],
            {
                "url": f"{self.portal_url}/registry-images/@@images/site_favicon/favicon.ico",
                "width": 72,
                "height": 72,
            },
        )

    def test_endpoint_store_logo_footer_dimensions_if_saved(self):
        image_file = os.path.join(os.path.dirname(__file__), "logo.png")
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read())
        filename = base64.b64encode(b"logo.png")
        self.api_session.patch(
            "/@controlpanels/site",
            json={
                "site_logo_footer": f"filenameb64:{filename.decode()};datab64:{image_data.decode()}",
            },
        )
        commit()

        self.assertEqual(441, self.site_proxy_additional.site_logo_footer_width)
        self.assertEqual(114, self.site_proxy_additional.site_logo_footer_height)

        resp = self.api_session.get("/@site").json()
        self.assertEqual(
            resp["plone.site_logo_footer"],
            {
                "url": f"{self.portal_url}/registry-images/@@images/site_logo_footer/logo.png",
                "width": 441,
                "height": 114,
            },
        )
