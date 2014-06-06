# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
from pytils import translit


class TranslitFileSystemStorage(FileSystemStorage):

    def get_valid_name(self, name):
        name = translit.translify(unicode(name))
        return super(TranslitFileSystemStorage, self).get_valid_name(name)
