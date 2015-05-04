# encoding: utf-8
from django import template
from utils.url import make_absolute_url as mau


register = template.Library()


@register.simple_tag
def make_absolute_url(path):
    """
    Divide the space description in two paragraphs.
    """
    return mau(path)