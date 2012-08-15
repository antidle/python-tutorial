#!/usr/bin/env python
# -*- utf-8 -*-

import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2
print s.random(0,9)  # Returns random 1~10

# Print list of available methods
print s.system.listMethods()

