class UpperAttrMetaClass(type):
    """docstring for UpperAttrMetaClass"""
    def __new__(upperattr_mateclass, future_class_name, future_class_parents, future_class_attr):

        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(upperattr_mateclass,future_class_name, future_class_parents, uppercase_attr)

class Foo(object):
    """docstring for foo"""
    __metaclass__=UpperAttrMetaClass
    def foo():
        print 'helloworld'
print hasattr(Foo, 'foo')

print hasattr(Foo, 'FOO')