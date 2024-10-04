# -*- coding: utf-8 -*-
from . import logger
from collective.volto.sitesettings.setuphandlers import post_install
from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info("Running upgrade (Python): Fix title field")

    post_install(api.portal.get())
