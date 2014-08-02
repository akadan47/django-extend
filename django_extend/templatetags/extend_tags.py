# coding: utf-8
from __future__ import division, absolute_import, unicode_literals

import os
import urlparse
from decimal import Decimal

from django import template
from django.conf import settings

from ..utils import str2bool

register = template.Library()


@register.simple_tag
def static(file_url_rel, **kwargs):
    add_timestamp = str2bool(kwargs.get('add_timestamp', 'no'))
    check_min = str2bool(kwargs.get('check_min', 'no'))
    file_url_abs = urlparse.urljoin(settings.STATIC_URL, file_url_rel)
    file_path = os.path.join(settings.STATIC_ROOT, file_url_rel)
    file_name, file_ext = os.path.splitext(file_path)
    if (file_ext in ['.css', '.js']) and (os.path.exists(file_path)):
        if check_min:
            file_path_min = file_path.replace(file_ext, '.min'+file_ext)
            if os.path.exists(file_path_min):
                file_path = file_path_min
                file_url_abs = file_url_abs.replace(file_ext, '.min'+file_ext)
        if add_timestamp:
            file_url_abs += '?%d' % os.path.getmtime(file_path)
    return file_url_abs


@register.filter
def key(d, key_name):
    return d[key_name]


@register.filter
def index(l, index):
    return l[index]


def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)


@register.filter
def sub(value, arg):
    """Subtracts the arg from the value."""
    try:
        return valid_numeric(value) - valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False


@register.filter
def mul(value, arg):
    """Multiplies the arg with the value."""
    try:
        return valid_numeric(value) * valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''
mul.is_safe = False


@register.filter()
def div(value, arg):
    """Divides the arg by the value."""
    try:
        return valid_numeric(value) / valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''
div.is_safe = False