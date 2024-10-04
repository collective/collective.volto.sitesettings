from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsAdditionalSiteSchema,
)
from collective.volto.sitesettings.utils import FIELD_MAPPING
from json.decoder import JSONDecodeError
from plone import api
from plone.formwidget.namedfile.converter import b64decode_file
from plone.registry.interfaces import IRegistry
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services.site.get import Site as BaseSite
from plone.restapi.services.site.get import SiteGet as BaseSiteGet
from zope.component import adapter
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import Interface

import json
import logging


logger = logging.getLogger(__name__)


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class Site(BaseSite):
    def __call__(self, expand=False):
        """"""
        # get standard fields
        result = super().__call__(expand=expand)

        registry = getUtility(IRegistry)
        additional_settings = registry.forInterface(
            ICollectiveVoltoSitesettingsAdditionalSiteSchema,
            prefix="plone",
            check=False,
        )

        # set title and subtitle based on language, if field is set
        result["site"]["plone.site_title"] = self.json_to_dict(
            additional_settings, "site_title_translated"
        )
        result["site"]["plone.site_subtitle"] = self.json_to_dict(
            additional_settings, "site_subtitle"
        )

        # images
        site_url = api.portal.get().absolute_url()
        for field, interface_name in FIELD_MAPPING.items():
            settings = registry.forInterface(
                interface_name, prefix="plone", check=False
            )
            value = self.get_value_from_registry(settings, field)
            result["site"][f"plone.{field}"] = {}
            if value:
                filename, data = b64decode_file(value)
                result["site"][f"plone.{field}"][
                    "url"
                ] = f"{site_url}/registry-images/@@images/{field}/{filename}"
                result["site"][f"plone.{field}"][
                    "width"
                ] = self.get_value_from_registry(additional_settings, f"{field}_width")
                result["site"][f"plone.{field}"][
                    "height"
                ] = self.get_value_from_registry(additional_settings, f"{field}_height")

        return result

    def get_value_from_registry(self, registry, field):
        try:
            return getattr(registry, field, "")
        except KeyError:
            return ""

    def json_to_dict(self, registry, field):
        data = self.get_value_from_registry(registry=registry, field=field)
        if not data:
            return {}
        try:
            return json.loads(data)
        except (JSONDecodeError, TypeError) as e:
            logger.exception(e)
            return {}


class SiteGet(BaseSiteGet):
    def reply(self):
        site = Site(self.context, self.request)
        return site(expand=True)["site"]
