#!/usr/bin/env python

from canari.maltego.entities import IPv4Address, Phrase
from common.entities import CookieGrabber, decryptCookie
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
    'dotransform'
]

#@superuser
@configure(
    label='LB IP to IPv4 Address',
    description='Converts Load Balancer IP to IPv4 Address Entity',
    uuids=[ 'cookieGrabber.v2.LBIP2IPv4Address' ],
    inputs=[ ( 'Web Sites', decryptCookie ) ],
    debug=True
)
def dotransform(request, response):

	buff = request.fields
	for key, value in buff.iteritems():
	  if key == 'lbip':
		e = IPv4Address(value)
		response += e
	  
		return response