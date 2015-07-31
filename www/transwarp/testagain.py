__author__ = 'Administrator'
#!/usr/bin/env python
#coding:utf-8
class LockContext(object):


    def __enter__(self):
        print 'Enter\n'

    def __exit__(self, type, value, traceback):
        print 'Exit out'


def hello():
    print 'now I\'m hello '

def hj():
    with LockContext():
        return hello()

hj()