__author__ = 'Administrator'
#!/usr/bin/env python
#coding:utf-8
class StringField(Field):

    """docstring for StringField"""

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'varchar(255)'

        super(StringField, self).__init__(**kw)