from django.contrib.sites.models import Site
from django.conf import settings
from urlparse import urljoin


def make_absolute_url(path):
    """
    Make a absolute url from given path.
    Use Site framework to know the domain
    """
    site = Site.objects.get_current()

    # TODO re-implement when needed
    # if settings.DEBUG:
    #     protocol = 'http://'
    # else:
    #     protocol = 'https://'

    protocol = 'http://'
    base_url = '{protocol}{site_url}'.format(
        protocol=protocol,
        site_url=site.domain
    )
    return urljoin(base_url, path)