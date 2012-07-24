#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
두 디렉토리의 이미지들을 비교하기 위한 html생성.
파일명이 같은 이미를 쌍으로 표시.
이미지가 너무 많으면 브라우저가 뻗어 버려서 만들어 두고 못썼음.
그래서 이거 안쓰고 대신에 Javascript로 페이징 하는 걸 만들었음.
'''

import os

DIR_BASE = "/Users/airless/Documents/pyCharmWorkspace/kaizoku/kaizoku/static/images/gokudo"
DIR_A = "240"
DIR_B = "360"

#os.chdir(DIR_BASE)
list_a = os.listdir(DIR_BASE + "/" + DIR_A)
list_b = os.listdir(DIR_BASE + "/" + DIR_B)
list_a.sort(key=lambda x: "%08s" % x)
list_b.sort(key=lambda x: "%08s" % x)
list_not_a = []

def rel_path (dname, fname):
    return "%s/%s" % (dname, fname)

print\
"""
<html>
<body>
"""
for aname in list_a:
    if list_b.count(aname) > 0:
        list_b.remove(aname)
    else:
        print "<div>"
        print aname
        print "<img src='%s' style='width:120px' />" % rel_path(DIR_A, aname)
        print "<img src='%s' style='width:160px' />" % rel_path(DIR_B, aname)
        print "</div>"

for bname in list_b:
    print "<div>"
    print bname
    print "<img src='%s' style='width:120px' />" % rel_path(DIR_A, bname)
    print "<img src='%s' style='width:160px' />" % rel_path(DIR_B, bname)
    print "</div>"

print\
"""
</body>
</html>
"""
