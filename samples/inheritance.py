#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

print ChildA(),ChildB()

self = ChildA() #??
Base.__init__(self) # 오, 이런 거도 되다니... 이제 어째..;;
