import mailchimp
from django.conf import settings


def get_mailchimp_api():
    if not hasattr(settings, 'MAILCHIMP_API_KEY'):
        raise KeyError('MAILCHIMP_API_KEY is not defined in settings')
    return mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)