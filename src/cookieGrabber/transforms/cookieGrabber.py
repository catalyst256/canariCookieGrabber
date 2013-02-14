#!/usr/bin/env python

import requests
import sys
import re
from canari.maltego.entities import Website
from canari.maltego.message import UIMessage
from common.entities import CookieGrabber, netscalerCookie
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Cookiegrabber Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]

#@superuser
@configure(
    label='To Search Netscaler Cookie',
    description='Searches a URL for Netscaler Cookies',
    uuids=[ 'cookieGrabber.v2.NetscalerCookie_fromURL' ],
    inputs=[ ( 'Reconnaissance', Website ) ],
    debug=True
)
def dotransform(request, response):
    
    r = requests.get('http://' +  request.value)
    cookie = str(r.cookies)
    #print cookie
    for s in re.finditer('NSC_([a-zA-Z0-9\_\.\-\:\=]*)=[0-9a-f]{8}([0-9a-f]{8})[a-f0-9]{24}([0-9a-f]{4})',cookie):
      if s is not None:
	e = netscalerCookie(s.group())
	e.enclbname = s.group(1)
	e.enclbip = s.group(2)
	e.enclbport = s.group(3)
	response += e
      else:
	print 'No Cookie Found'
    return response  


def onterminate():
    pass