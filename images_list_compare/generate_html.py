#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
두 디렉토리의 이미지들을 비교하기 위한 html생성.
파일명이 같은 이미를 쌍으로 표시.
'''

import os

DIR_BASE = "/Users/airless/Documents/pyCharmWorkspace/kaizoku/kaizoku/static/images/gokudo"
DIR_A = "240"
DIR_B = "360"
YAKUZA_IDS_FILE = "ids.txt"

with open(YAKUZA_IDS_FILE) as f:
    ids = f.readlines()

def rel_path (dname, fname):
    return "%s/%s.gif" % (dname, fname)

print\
"""
<html>
<body>
"""
for id in ids:
    id = id.rstrip()
    print "<div>"
    print id + ":"
    print "<img src='%s' style='width:120px' />" % rel_path(DIR_A, id)
    print "<img src='%s' style='width:160px' />" % rel_path(DIR_B, id)
    print "</div>"

print\
"""
</body>
</html>
"""
