class A:

    @classmethod
    def class_foo(cls, x):
        print "class_foo called with %s" % x
        cls.static_foo(x)

    @staticmethod
    def static_foo(x):
        print "static_foo called with %s" % x

    @staticmethod
    def _static_foo(x):
        print "_static_foo called with %s" % x

    @classmethod
    def _class_foo(cls, x):
        print "_class_foo called with %s" % x
        cls.static_foo(x)

    def _private_foo(self, x):
        print "_private_foo called with %s" % x

a = A()
A.class_foo(10)
A._static_foo(10)
A._class_foo(10)
a._private_foo(10)
