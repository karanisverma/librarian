"""
homepage.py: Flat pages used for web demo only

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""


def routes(app):
    return (
        (
            'flat:how_to_connect',
            app.exts.flat_pages.how_to_connect,
            ['GET'],
            '/how-to-connect/',
            {}
        ), (
            'flat:how_to_lantern',
            app.exts.flat_pages.lantern,
            ['GET'],
            '/how-to-connect/lantern/',
            {}
        ), (
            'flat:how_to_pillar',
            app.exts.flat_pages.pillar,
            ['GET'],
            '/how-to-connect/pillar/',
            {}
        ), (
            'flat:about',
            app.exts.flat_pages.pillar,
            ['GET'],
            '/about-outernet/',
            {}
        )

    )
