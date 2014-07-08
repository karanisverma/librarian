"""
migrations.py: functions for managing migrations

Copyright 2014, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import os
import re
import sqlite3
from functools import wraps
from itertools import dropwhile
from contextlib import contextmanager

from .squery import transaction, query
from . import __version__ as _version, __author__ as _author


__version__ = _version
__author__ = _author
__all__ = ('transaction', 'connect', 'disconnect', 'get_migrations',
           'get_migration_version', 'run_migration', 'migrate')


MTABLE = 'migrations'   # SQL table in which migration data is stored
MIGRATION_FILE_RE = re.compile('^\d{2}_[^.]+\.sql$')


def get_migrations(path, min_ver=0):
    """ Get migration files from specified path

    :param path:    path containing migration files
    :param min_ver: minimum migration version
    :returns:       return an iterator that returns only items whose versions
                    are >= min_ver
    """
    int_first_two = lambda s: int(s[:2])

    paths = [(os.path.join(path, f), int_first_two(f))
             for f in os.listdir(path)
             if MIGRATION_FILE_RE.match(f)]
    paths.sort(key=lambda x: x[1])
    return dropwhile(lambda x: x[1] < min_ver, paths)


def get_migration_version():
    """ Query database and return migration version """
    qry = 'select version from %s where id == 0;' % MTABLE
    try:
        cur = query(qry)
    except sqlite3.OperationalError as err:
        if 'no such table' in str(err):
            return -1
        raise
    return cur.fetchone()[0]


def run_migration(path, version):
    """ Run migration script

    :param path:    path of the migration script
    :param version: version number of the migration
    """
    with open(path, 'r') as script:
        sql = script.read()
    with transaction() as cur:
        cur.executescript(sql)
        qry = 'replace into %s (id, version) values (?, ?)' % MTABLE
        query(qry, 0, version, cursor=cur)


def migrate(path):
    """ Run all migrations that have not been run

    Migrations will be run inside a transaction.

    :param path:    path that contains migrations
    """
    ver = get_migration_version()
    migrations = get_migrations(path, ver + 1)
    for path, version in migrations:
        run_migration(path, version)
        print("Completed migration %s" % version)
