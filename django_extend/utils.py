# coding: utf-8
import os
import datetime
from django.utils.encoding import force_unicode, smart_str


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def cyr2lat(text):
    result = str()
    cyr_map = {
        u'а': u'a', u'б': u'b', u'в': u'v', u'г': u'g', u'д': u'd', u'е': u'e', u'ё': u'yo', u'ж': u'zh',
        u'з': u'z', u'и': u'i', u'й': u'j', u'к': u'k', u'л': u'l', u'м': u'm', u'н': u'n', u'о': u'o',
        u'п': u'p', u'р': u'r', u'с': u's', u'т': u't', u'у': u'u', u'ф': u'f', u'х': u'h', u'ц': u'c',
        u'ч': u'ch', u'ш': u'sh', u'щ': u'sh', u'ъ': u'', u'ы': u'y', u'ь': u'', u'э': u'e', u'ю': u'yu',
        u'я': u'ya',
        u'А': u'A', u'Б': u'B', u'В': u'V', u'Г': u'G', u'Д': u'D', u'Е': u'E', u'Ё': u'Yo', u'Ж': u'Zh',
        u'З': u'Z', u'И': u'I', u'Й': u'J', u'К': u'K', u'Л': u'L', u'М': u'M', u'Н': u'N', u'О': u'O',
        u'П': u'P', u'Р': u'R', u'С': u'S', u'Т': u'T', u'У': u'U', u'Ф': u'F', u'Х': u'H', u'Ц': u'C',
        u'Ч': u'Ch', u'Ш': u'Sh', u'Щ': u'Sh', u'Ъ': u'', u'Ы': u'Y', u'Ь': u'', u'Э': u'E', u'Ю': u'Yu',
        u'Я': u'Ya'
    }
    for x in text:
        if x in cyr_map:
            result += cyr_map[x]
        elif x in (' ', '_', '-'):
            if not result.endswith('_'):
                result += '_'
        elif (48 <= ord(x) <= 57) or (65 <= ord(x) <= 90) or (97 <= ord(x) <= 122):
            result += x
    return result


def normalize_filename(upload_to, name_field, instance, filename):
    upload_to = '%s/' % os.path.normpath(force_unicode(datetime.datetime.now().strftime(smart_str(upload_to))))
    name, ext = os.path.splitext(filename)
    name = cyr2lat(name)
    max_length = instance.__class__.__dict__.get(name_field).field.max_length
    max_length = int(max_length) - len(upload_to) - len(ext)
    name = name[:max_length]
    filename = ''.join([name, ext]).lower()
    return upload_to + filename