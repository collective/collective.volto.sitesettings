from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsAdditionalSiteSchema,
)
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer

import json


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.volto.sitesettings:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["collective.volto.sitesettings.upgrades"]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    registry = getUtility(IRegistry)
    additional_settings = registry.forInterface(
        ICollectiveVoltoSitesettingsAdditionalSiteSchema,
        prefix="plone",
        check=False,
    )
    # copy site title into the custom one
    site_title = registry["plone.site_title"]
    site_title_translated = getattr(additional_settings, "site_title_translated", "")

    if site_title_translated:
        site_title_translated = json.loads(site_title_translated)
    else:
        site_title_translated = {}

    for lang in registry["plone.available_languages"]:
        if not site_title_translated.get(lang, ""):
            site_title_translated[lang] = site_title

    additional_settings.site_title_translated = json.dumps(site_title_translated)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
