from collective.volto.sitesettings.interfaces import IRegistryImagesView
from collective.volto.sitesettings.utils import FIELD_MAPPING
from plone.formwidget.namedfile.converter import b64decode_file
from plone.namedfile.browser import Download
from plone.namedfile.file import NamedImage
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from zope.component import getUtility
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces import NotFound


@implementer(IRegistryImagesView)
class RegistryImagesView(BrowserView):
    """"""

    def __call__(self):
        return


@implementer(IPublishTraverse)
class ImagesView(Download):
    def __init__(self, context, request):
        super().__init__(context=context, request=request)
        self.data = None

    def publishTraverse(self, request, name):
        super().publishTraverse(request=request, name=name)

        if self.fieldname:
            registry = getUtility(IRegistry)
            registry_interface = FIELD_MAPPING.get(self.fieldname, None)
            if not registry_interface:
                raise NotFound(self, "a", self.request)
            settings = registry.forInterface(registry_interface, prefix="plone")
            value = getattr(settings, self.fieldname, None)
            if value:
                filename, data = b64decode_file(value)
                data = NamedImage(data=data, filename=filename)
                self.data = data
        return self

    def _getFile(self):
        if not self.data:
            raise NotFound(self, "b", self.request)
        return self.data
