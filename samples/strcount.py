#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

result = {}
for line in sys.stdin:
    num = line.strip()
    if not result.has_key(num):
        result[num] = 0
    result[num] += 1

for key in sorted(result.iterkeys()):
    print "%s: %d" % (key, result[key])
