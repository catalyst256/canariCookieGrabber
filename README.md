# README - Cookiegrabber

Pre-reqs:

Maltego (community or paid) I've tested on Maltego Radium CE 3.3.0
Canari Framework (https://github.com/allfro/canari)

I've tested this on Windows 7 64x bit running python 2.6 (32 bit) and on Backtrack 5.

The following modules are required (and may already exist on your systems):

import requests
import sys
import re
from string import maketrans, ascii_letters

This is a Canari Framework (http://www.canariproject.com/) Maltego Local Transform package that takes the Python based Netscaler Cookie Decrypter I created last year and allows it to be used in Maltego.

To install the package download from my github repo (however you chose to do that). Browse to the folder and run:

python setup.py install

You should then be able to run:

canari install-package cookieGrabber

This will install the transforms and entity objects for the package.

Within Maltego you should have a new Entity category called "Cookies" with 2 objects.

To use the transforms, create a website object, right click and under Transforms there should be a Reconnaissance section with a transform called "To Search Netscaler Cookie".

If the website uses a Netscaler for load balancing persistence (they start with NSC_) it will return a new entity (or two).

If a Netscaler Cookie entity is returned (it looks like a cookie), you can then run the other transform that decrypts the cookie and returns, load balancer name, load balancer ip and port.

The code isn't pretty but it works so if you find any bugs let me know.

catalyst256@gmail.com
@catalyst256

To Do:

Currently only works on http ports, need to add https as well
Add cookies for F5 load balancers and decryption as well


