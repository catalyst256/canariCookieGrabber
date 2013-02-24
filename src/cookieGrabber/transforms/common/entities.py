#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Cookiegrabber Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'Cookiegrabber',
    'netscalerCookie'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyCookiegrabberEntity will
have an entity type name of cookieGrabber.MyCookiegrabberEntity. When adding a new entity in Maltego, you will have to specify this
name (cookieGrabber.MyCookiegrabberEntity) in the 'Unique entity type' field.
"""
class CookieGrabber(Entity):
    namespace = 'cookieGrabber'
  
  
@EntityField(name='nscookie.lbname', propname='enclbname', displayname='Encrypted LB Name' ,type=EntityFieldType.String)
@EntityField(name='nscookie.lbip', propname='enclbip', displayname='Encrypted LB IP' ,type=EntityFieldType.String)
@EntityField(name='nscookie.lbport', propname='enclbport', displayname='Encrypted LB Port' ,type=EntityFieldType.String)

class netscalerCookie(CookieGrabber):
  pass



@EntityField(name='lbip',propname='lbip', displayname='Load Balancer IP')
@EntityField(name='lbport',propname='lbport', displayname='Load Balancer Port')

class decryptCookie(CookieGrabber):
  pass