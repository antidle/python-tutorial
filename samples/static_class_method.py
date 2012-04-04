class A:

    @classmethod
    def class_foo(cls, x):
        print "class_foo called with %s" % x
        static_foo(x)

    @staticmethod
    def static_foo(x):
        print "static_food called with %s" % x

a = A()
A.class_foo(10)

