#!/usr/bin/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://127.0.0.1:1325')

server.quit()
