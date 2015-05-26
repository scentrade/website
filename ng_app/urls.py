from django.conf.urls import patterns, include, url
from ng_app.views import (PartialGroupView, ContactView, FreeTrialView)


templates = [
    'sections/about-us.html',
    'sections/products.html',
    'sections/home.html',
    'sections/blog.html',
    'sections/blog-single.html',
    # Directives
    'directives/owl-carousel.html']

partial_patterns = patterns('')

for template in templates:
    partial_patterns += patterns('',
        url(r'^{0}$'.format(template),
            PartialGroupView.as_view(
                template_name='ng_app/partials/{0}'.format(template))),
    )

urlpatterns = patterns('',
    url(r'^partials/', include(partial_patterns, namespace='partials')),
    url(r'^partials/sections/contact.html',
        ContactView.as_view(), name='contact'),
    url(r'^partials/homepage.html',
        FreeTrialView.as_view(
            template_name='ng_app/partials/homepage.html'),
        name='homepage'),
    url(r'^partials/sections/services.html',
        FreeTrialView.as_view(
            template_name='ng_app/partials/sections/services.html'),
        name='services'),
)