"""
plugins: code related to plugins and plugin loaders

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import os
import logging

import bottle
from bottle import static_file

from .exceptions import NotSupportedError

PLUGINS_PATH = os.path.dirname(__file__)
INSTALLED = {}
DASHBOARD = []


def get_plugin_list(conf, config_param):
    return [p.strip().lower()
            for p in conf.get(config_param, '').split(',')]


def get_module_path(module):
    return os.path.dirname(os.path.abspath(module.__file__))


def route_plugin(app, mod):
    """ Return a function for routing plugin routes

    The route information must be in the following format::

        (name, callback,
         method, path, route_configuration)

    The path is always prefixed with ``/p/module_name/``. For instance, if your
    route has a path of ``/bar``, and is called ``foo``, it will be remapped to
    ``/p/foo/bar``.

    Similarily to paths, names are also modified. The ``plugins:`` prefix. For
    a plugin module ``foo`` and route name of ``bar``, we therefore get a full
    route name that spells ``plugins:foo:bar``.

    :param app:     app for which to create the routing function
    :param mod:     name of the plugin module
    :returns:       routing function
    """
    def _route_plugin(*routes):
        for route in routes:
            name, callback, method, path, kw = route
            name = 'plugins:%s:%s' % (mod, name)
            path = ('/p/%s/' % mod) + path.lstrip('/')
            app.route(path, method, callback, name=name, **kw)
    return _route_plugin


def install_views(mod_path):
    """ Add view lookup path if plugin has views directory

    :param mod_path:  absolute path to module
    """
    view_path = os.path.join(mod_path, 'views')
    if not os.path.isdir(view_path):
        return
    bottle.TEMPLATE_PATH.insert(1, view_path)


def install_static(app, mod_name, mod_path):
    """ Add routes for plugin static if plugin contains a static directory

    All routes are mapped to urls that start with ``/s/`` prefix followed by
    module name. So, for a plugin called ``foo``, we get ``js/main.js`` asset
    by using the following path: ``/s/foo/js/main.js``.

    Each route is also given a name with ``plugins:`` prefix and ``:static``
    suffix added to the module name. Fof a module called ``foo``, the route
    name is ``plugins:foo:static``.

    :param app:       application object
    :param mod_name:  module name
    :param mod_path:  absolute path to module
    """
    static_path = os.path.join(mod_path, 'static')
    if not os.path.isdir(static_path):
        return

    def _route_plugin_static(path):
        return static_file(path, static_path)
    _route_plugin_static.__name__ = '_route_%s_static' % mod_name

    app.route('/s/%s/<path:path>' % mod_name, 'GET', _route_plugin_static,
              name='plugins:%s:static' % mod_name, no_i18n=True)


def install_plugins(app):
    conf = app.config
    to_install = get_plugin_list(conf, 'plugins.enabled')
    dashboard = get_plugin_list(conf, 'dashboard.plugins')
    # Import each plugin module and initialize it
    for mod_name in to_install:
        try:
            plugin = getattr(__import__(mod_name, fromlist=['plugin']),
                             'plugin')
            logging.debug("Plugin '%s' loaded", mod_name)
        except (ImportError, AttributeError) as err:
            logging.error("Plugin '%s' could not be loaded, skipping (reason: "
                          "%s)", mod_name, err)
            continue
        except NotSupportedError as err:
            logging.error(
                "Plugin '%s' not supported, skipping (reason: %s)", mod_name,
                err.reason)
            continue

        try:
            plugin.install(app, route_plugin(app, mod_name))
        except NotSupportedError as err:
            logging.error(
                "Plugin '%s' not supported, skipping (reason: %s)", mod_name,
                err.reason)
            continue
        except AttributeError:
            print('attrerror')
            logging.error("Plugin '%s' not correctly implemented, skipping",
                          mod_name)
            continue

        mod_path = get_module_path(plugin)
        install_views(mod_path)
        install_static(app, mod_name, mod_path)

        INSTALLED[mod_name] = plugin
        logging.info('Installed plugin %s', mod_name)

    # Install dashboard plugins for plugins that have them
    logging.debug("Installing dashboard plugins: %s", ', '.join(dashboard))
    for p in dashboard:
        if p not in INSTALLED:
            logging.debug("Plugin '%s' is not installed, ignoring", p)
            continue
        plugin = INSTALLED[p]
        try:
            DASHBOARD.append(plugin.Dashboard())
            logging.info('Installed dashboard plugin %s', p)
        except AttributeError:
            logging.debug("No dashboard plugin for '%s'", p)
            continue
