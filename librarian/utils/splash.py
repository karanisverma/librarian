"""
splash.py: Librarian loading splash screen

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import multiprocessing

from os.path import dirname, join
from wsgiref.simple_server import make_server

import bottle


TEMPLATE_ROOT = join(dirname(dirname(__file__)), 'views')
splash_app = bottle.Bottle()


@splash_app.route('<path:re:.+>')
def splash_route(path):
    return bottle.mako_template(join(TEMPLATE_ROOT, 'splash'))


class SplashServer(object):

    def serve(self, host, port):
        server = make_server(host, port, splash_app)
        server.serve_forever()

    def start(self, config):
        host = config['splash.bind']
        port = config['splash.port']
        self.process = multiprocessing.Process(target=self.serve,
                                               args=(host, port))
        self.process.start()

    def stop(self):
        self.process.terminate()


splash_server = SplashServer()
