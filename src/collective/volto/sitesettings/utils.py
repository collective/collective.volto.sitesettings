from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsAdditionalSiteSchema,
)
from plone.base.interfaces.controlpanel import ISiteSchema


FIELD_MAPPING = {
    "site_logo": ISiteSchema,
    "site_logo_footer": ICollectiveVoltoSitesettingsAdditionalSiteSchema,
    "site_favicon": ISiteSchema,
}
