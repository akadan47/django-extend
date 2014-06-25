# coding: utf-8
from django.contrib import admin


class InitialFieldsMixin(object):
    def get_form(self, request, obj=None, **kwargs):
        form = admin.ModelAdmin.get_form(self, request, obj, **kwargs)
        if not hasattr(self.__class__, 'initial'):
            return form
        old_init = form.__init__

        def new_init(_self, *args, **kwargs):
            if 'instance' not in kwargs and 'initial' in kwargs:
                for field_name, callback in self.__class__.initial.iteritems():
                    kwargs['initial'][field_name] = callback(self, request, obj, **kwargs)
            return old_init(_self, *args, **kwargs)
        form.__init__ = new_init

        return form
