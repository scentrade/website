from django.conf.urls import *
from rest_framework import routers
from company.viewsets import ClientViewSet, TestimonyViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'clients', ClientViewSet)
router.register(r'testimonials', TestimonyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]