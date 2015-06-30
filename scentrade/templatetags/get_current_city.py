from django import template
from django.contrib.gis.geoip import GeoIP


register = template.Library()


@register.simple_tag(takes_context=True)
def get_current_city(context):
    request = context['request']
    ip = request.META.get('REMOTE_ADDR', None)
    print ip
    g = GeoIP()
    country = g.country(ip)
    print country
    return country['country_name']