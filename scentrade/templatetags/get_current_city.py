from django import template
from django.contrib.gis.geoip import GeoIP


register = template.Library()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@register.simple_tag(takes_context=True)
def get_current_city(context):
    request = context['request']
    ip = get_client_ip(request)
    print ip
    g = GeoIP()
    country = g.country(ip)
    print country
    return country['country_name']