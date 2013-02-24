#!/usr/bin/env python

import sys
import re
import string
from string import maketrans, ascii_letters
from common.entities import CookieGrabber, netscalerCookie, decryptCookie
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
    label='To Decrypt Netscaler Cookie',
    description='Takes the encrypted Netscaler Cookie and decrypts it',
    uuids=[ 'decryptCookie.v2.cookieToclearText' ],
    inputs=[ ( 'Web Sites', netscalerCookie ) ],
    debug=True
)
def dotransform(request, response):
    
    buff = request.fields
    for key, value in buff.iteritems():
	  s = str(key + '='+ value)
	  #print s
	  for t in re.finditer('NSC_([a-zA-Z0-9\_\.\-\:\=]*)=[0-9a-f]{8}([0-9a-f]{8})[a-f0-9]{24}([0-9a-f]{4})',s):
		servicename = t.group(1)
		serverip = int(t.group(2), 16)
		serverport = int(t.group(3), 16)
		
		trans = maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ','zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY')
		realname = servicename.translate(trans)
		
		ipkey = 0x03081e11
		decodedip = hex (serverip ^ ipkey)
		p = decodedip[2:10].zfill(8)
		realip = '.'.join(str(int(i, 16)) for i in([p[i:i+2] for i in range(0, len(p), 2)]))
		
		portkey = 0x3630
		decodedport = serverport ^ portkey #no need to convert to hex since an integer will do for port
		realport = str(decodedport)
		
		e = decryptCookie(realname)
		#e.lbname = realname
		e.lbip = realip
		e.lbport = realport
		response += e
    
    return response


def onterminate():

    pass