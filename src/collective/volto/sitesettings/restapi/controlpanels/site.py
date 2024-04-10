from collective.volto.sitesettings.interfaces import ICollectiveVoltoSitesettingsLayer
from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsSiteControlpanel,
)
from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsSiteSchema,
)
from plone.restapi.controlpanels.registry import (
    SiteControlpanel as SiteControlpanelBase,
)
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(Interface, ICollectiveVoltoSitesettingsLayer)
@implementer(ICollectiveVoltoSitesettingsSiteControlpanel)
class SiteControlpanel(SiteControlpanelBase):
    schema = ICollectiveVoltoSitesettingsSiteSchema
