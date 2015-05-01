from django.conf.urls import patterns, include, url
from ng_app.views import (PartialGroupView)


templates = [
    'homepage.html']

partial_patterns = patterns('')

for template in templates:
    partial_patterns += patterns('',
        url(r'^{0}$'.format(template),
            PartialGroupView.as_view(
                template_name='ng_app/partials/{0}'.format(template))),
    )

urlpatterns = patterns('',
    url(r'^partials/', include(partial_patterns, namespace='partials')),
)