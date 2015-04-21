from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)