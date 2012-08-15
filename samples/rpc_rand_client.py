#!/usr/bin/env python
# -*- utf-8 -*-

import sys
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')

if len(sys.argv) != 4:
    print "%s 1: min, 2: max, 3: try count" % sys.argv[0]

    sys.exit(1)

for i in range(0, int(sys.argv[3])):
    print s.random(int(sys.argv[1]),int(sys.argv[2]))
