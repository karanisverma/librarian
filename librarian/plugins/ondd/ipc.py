"""
ipc.py: make XML IPC to ondd via its control socket

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from __future__ import unicode_literals

import socket
import logging
import xml.etree.ElementTree as ET
from contextlib import contextmanager

from bottle import request

from ...lib.html import yesno

OUT_ENCODING = 'ascii'
IN_ENCODING = 'utf8'

NA_KU_OFF = 10750  # Frequency offset for North America Ku
UN_LO_OFF = 9750  # Low band offset
UN_HI_OFF = 10600  # High band offset
UN_HI_SW = 11700  # Transponder frequency at which we switch to high band


def connect(path):
    sock = socket.socket(socket.AF_UNIX)
    sock.connect(path)
    return sock


@contextmanager
def open_socket():
    sock = connect(request.app.config['ondd.socket'])
    try:
        yield sock
    finally:
        # Permanently close this socket
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()


def read(sock, buffsize=2014):
    """ Read the data from a socket until exhausted or NULL byte

    :param sock:        socket object
    :param buffsize:    size of the buffer (1024 by default)
    """
    idata = data = sock.recv(buffsize)
    while idata and '\0' not in idata:
        idata = sock.recv(buffsize)
        data += idata
    return data[:-1].decode(IN_ENCODING)


def parse(data):
    """ Parse incoming XML into Etree object

    :param data:    XML string
    :returns:       root node object
    """
    return ET.fromstring(data)


def send(payload):
    """ Connect to socket configured in the config file

    According to ONDD API, payload must be terminated by NULL byte. If the
    supplied payload isn't terminated by NULL byte, one will automatically be
    appended to the end.

    :param payload:     the XML payload to send down the pipe
    :returns:           response data
    """
    if not payload[-1] == '\0':
        payload = payload.encode(OUT_ENCODING) + '\0'
    with open_socket() as sock:
        logging.debug('ONDD: sending payload: %s', payload)
        sock.send(payload)
        data = read(sock)
        logging.debug('ONDD: received data: %s', data[:-1])
    return parse(data)


def xml_get_path(path):
    """ Return XML for getting a path

    :param path:    path of the get request
    """
    return '<get uri="%s" />' % path


def xml_put_path(path, subtree=''):
    """ Return XML for putting a path

    :param path:        path
    :param subtree:     XML fragment for the PUT request
    """
    return '<put uri="%s">%s</put>' % (path, subtree)


def kw2xml(**kwargs):
    """ Convert any keyword parameters to XML

    This function does not guarantee the order of the tags.

    Example::

        >>> kw2xml(foo='bar', bar='baz', baz=1)
        '<foo>bar</foo><bar>baz</bar><baz>1</baz>'

    """
    xml = ''
    for k, v in kwargs.items():
        xml += '<%(key)s>%(val)s</%(key)s>' % dict(key=k, val=v)
    return xml


def v2pol(volts):
    if volts == '13':
        return 'v'
    elif volts == '18':
        return 'h'
    return '0'


def get_status():
    """ Get ONDD status """
    payload = xml_get_path('/status')
    root = send(payload)
    tuner = root.find('tuner')
    net = root.find('network')
    return {
        'has_lock': tuner.find('lock').text == 'yes',
        'signal': int(tuner.find('signal').text),
        'snr': float(tuner.find('snr').text),
        'streams': [
            {'id': s.find('ident').text,
             'bitrate': int(s.find('bitrate').text)}
            for s in net]
    }


def get_file_list():
    """ Get ONDD file download list """
    payload = xml_get_path('/files/')
    try:
        root = send(payload)
    except ET.ParseError:
        logging.error('ONDD: Could not parse XML data')
        return []
    out = []
    flist = root.find('files')
    for f in flist:
        out.append({
            'path': f.find('path').text,
            'size': int(f.find('size').text),
            'progress': int(f.find('progress').text),
        })
    return out


def freq_conv(freq, lnb_type):
    """ Converts transponder frequency to L-band frequency

    The conversion formula requires the LNB type. The type can be either `'k'`
    for North America Ku band LNB or `'u'` for Universal LNB.

    Example:

        >>> freq_conv(11471, 'u')
        1721

    """
    if lnb_type == 'k':
        # NA Ku band LNB
        return freq - NA_KU_OFF
    # Universal
    if freq > UN_HI_SW:
        return freq - UN_HI_OFF
    return freq - UN_LO_OFF


def needs_tone(freq, lnb_type):
    """ Whether LNB needs a 22KHz tone

    Always returns ``True`` for North America Ku band LNBs.
    """
    if lnb_type == 'k':
        return True
    return freq > UN_HI_SW


def get_settings():
    """ Get ONDD tuner settings """
    payload = xml_get_path('/settings')
    root = send(payload)
    tuner = root.find('tuner')
    return {
        'frequency': int(tuner.find('frequency').text),
        'delivery': tuner.find('delivery').text,
        'modulation': tuner.find('modulation').text,
        'polarization': v2pol(tuner.find('voltage').text),
        'tone': tuner.find('tone').text == 'yes',
        'azimuth': int(tuner.find('azimuth').text or 0),
    }


def set_settings(frequency, symbolrate, delivery='dvb-s', modulation='qpsk',
                 tone=True, voltage=13, azimuth=0):
    tone = yesno(tone)
    payload = xml_put_path('/settings', kw2xml(**locals()))
    resp = send(payload)
    resp_code = resp.get('code')
    logging.debug('ONDD: received response code %s', resp_code)
    return resp_code