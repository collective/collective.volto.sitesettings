# -*- coding: utf-8 -*-
from . import logger
from collective.volto.sitesettings.interfaces import (
    ICollectiveVoltoSitesettingsAdditionalSiteSchema,
)
from collective.volto.sitesettings.setuphandlers import post_install
from plone import api
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import json


# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info("Running upgrade (Python): Fix title field")

    post_install(api.portal.get())
