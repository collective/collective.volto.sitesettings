from collective.volto.sitesettings import _
from plone.autoform import directives as form
from plone.restapi.controlpanels import IControlpanel
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Bytes
from zope.schema import Int
from zope.schema import SourceText


try:
    from plone.base.interfaces.controlpanel import ISiteSchema
except ImportError:
    # Plone 52
    from Products.CMFPlone.interfaces import ISiteSchema


class ICollectiveVoltoSitesettingsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveVoltoSitesettingsAdditionalSiteSchema(Interface):
    """
    Settings interface that add some extra fields to site controlpanel.
    """

    site_title_translated = SourceText(
        title=_("site_localized_label", default="Site title"),
        description=_(
            "site_localized_help",
            default="Translate site title for different available languages.",
        ),
        required=False,
        default="{}",
    )

    site_subtitle = SourceText(
        title=_("site_subtitle_label", default="Site subtitle"),
        description=_(
            "site_subtitle_help",
            default="",
        ),
        required=False,
        default="{}",
    )

    site_logo_footer = Bytes(
        title=_("logo_footer_label", default="Footer logo"),
        description=_(
            "logo_footer_help",
            default="Insert a logo that will be used in the site footer.",
        ),
        required=False,
    )

    site_logo_width = Int(required=False)
    site_logo_height = Int(required=False)
    site_favicon_width = Int(required=False)
    site_favicon_height = Int(required=False)
    site_logo_footer_width = Int(required=False)
    site_logo_footer_height = Int(required=False)


class ICollectiveVoltoSitesettingsSiteSchema(
    ISiteSchema, ICollectiveVoltoSitesettingsAdditionalSiteSchema
):
    """"""

    form.order_before(site_title_translated="site_logo")
    form.order_after(site_subtitle="site_title_translated")
    form.order_after(site_logo_footer="site_logo")

    form.omitted("site_title")
    form.omitted("site_logo_width")
    form.omitted("site_logo_height")
    form.omitted("site_favicon_width")
    form.omitted("site_favicon_height")
    form.omitted("site_logo_footer_width")
    form.omitted("site_logo_footer_height")


class ICollectiveVoltoSitesettingsSiteControlpanel(IControlpanel):
    """ """


class IRegistryImagesView(Interface):
    """
    Marker interface for view
    """
