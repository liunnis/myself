#!/usr/bin/env python
import urllib2
LOGIN = 'wesc'
PASSWORD = 'you"11NeverGuess'
URL = 'http://localhost'


def handler_version(url):
    from urlparse import urlparse as up
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWORD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWORD)[:-1])
    req.add_header("Authorization", "Basic %s" % b64str)
    return req
for funcType in ('handler', 'request'):
    print '***Using %s:' % funcType.upper()
    url = eval('%s:_version' % URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()
