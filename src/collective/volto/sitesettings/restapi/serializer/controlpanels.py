from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsSiteControlpanel,
)
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.serializer.controlpanels import ControlpanelSerializeToJson
from zope.component import adapter
from zope.interface import implementer


@implementer(ISerializeToJson)
@adapter(ICollectiveVoltoSitesettingsSiteControlpanel)
class VoltoSiteSettingsSerializeFromJson(ControlpanelSerializeToJson):
    def __call__(self):
        try:
            return super().__call__()
        except KeyError:
            # upgrade-step not yet launched, do not break endpoint
            return {
                "@id": f"{self.controlpanel.context.absolute_url()}/@controlpanels/{self.controlpanel.__name__}",
                "title": self.controlpanel.title,
                "group": self.controlpanel.group,
                "schema": {
                    "properties": [],
                    "fieldsets": [{"fields": []}],
                    "required": [],
                },
                "data": {},
            }
