#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

min = 1
max = 10
result ={}
for i in range(1, 10000):
    r = random.randint(min, max)
    if not result.has_key(r):
        result[r] = 0
    result[r] += 1

print result

