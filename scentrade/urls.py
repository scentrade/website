from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^sitemap\.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
#   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^', include('ng_app.urls', namespace='ng_app')),
    url(r'^api/', include('api.urls', namespace='api')),
    # (r'^search/', include('haystack.urls')),
    url(r'^.*$', TemplateView.as_view(template_name='base.html'), name='home'),
)