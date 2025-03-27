# -*- coding: utf-8 -*-


def upgrade(setup_tool=None):
    """ """
    setup_tool.runImportStepFromProfile(
        "profile-collective.volto.sitesettings:default",
        "plone.app.registry",
        run_dependencies=False,
    )
