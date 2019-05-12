from django import template
from django.conf import settings
from django.utils import formats
from django.utils.dateformat import format
from django.utils.timezone import get_default_timezone

register = template.Library()


@register.filter(expects_localtime=True, is_safe=False)
def thaidate(value, arg=None):
    if value in (None, ''):
        return ''

    try:
        arg = arg.replace('y', str(value.year + 543)[2:])
        arg = arg.replace('Y', str(value.year + 543))
    except:
        pass

    try:
        return formats.date_format(value, arg)
    except AttributeError:
        try:
            return format(value, arg)
        except AttributeError:
            return ''
