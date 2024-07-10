.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.volto.sitesettings/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.volto.sitesettings/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.volto.sitesettings/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.volto.sitesettings?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.volto.sitesettings/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.volto.sitesettings

.. image:: https://img.shields.io/pypi/v/collective.volto.sitesettings.svg
    :target: https://pypi.python.org/pypi/collective.volto.sitesettings/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.volto.sitesettings.svg
    :target: https://pypi.python.org/pypi/collective.volto.sitesettings
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.volto.sitesettings.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.volto.sitesettings.svg
    :target: https://pypi.python.org/pypi/collective.volto.sitesettings/
    :alt: License


=============================
collective.volto.sitesettings
=============================

Plone addon that extends @site controlpanel by adding new fields.

This product is the backend part of volto-site-settings_.

.. _volto-site-settings: https://github.com/collective/volto-site-settings

Features
--------

- Can set site title in different languages
- Can set a subtitle in different languages
- Can add a logo footer

It overrides `@site` endpoint to expose these new data.


Translations
------------

This product has been translated into

- Italian


Installation
------------

Install collective.volto.sitesettings by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.volto.sitesettings


and then running ``bin/buildout``


Authors
-------

Provided by awesome people ;)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.volto.sitesettings/issues
- Source Code: https://github.com/collective/collective.volto.sitesettings
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
