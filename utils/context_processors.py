from django.conf import settings
from django.contrib.gis.geoip import GeoIP


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_current_country(request):
    ip = get_client_ip(request)
    g = GeoIP()
    country = g.country(ip)
    country_code = country['country_code']
    if country_code == 'MX':
        return country_code
    # By default show content for Colombia
    return 'CO'


def global_variables(request):
    """
    Global variables available in all templates
    """
    data = {
        'DEBUG': settings.DEBUG,
        'CURRENT_COUNTRY': get_current_country(request),
    }
    return data