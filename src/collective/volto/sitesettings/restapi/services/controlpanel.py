from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsSiteControlpanel,
)
from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsSiteSchema,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(Interface, Interface)
@implementer(ICollectiveVoltoSitesettingsSiteControlpanel)
class SiteSettings(RegistryConfigletPanel):
    schema = ICollectiveVoltoSitesettingsSiteSchema
    configlet_id = "VoltoSiteSettings"
    configlet_category_id = "Products"
    schema_prefix = None
