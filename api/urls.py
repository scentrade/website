from django.conf.urls import *
from rest_framework import routers
from company.viewsets import (ClientViewSet, TestimonyViewSet)
from store.views import (AddProductToCartView, RemoveProductFromCartView,
                         ShoppingCartView)
from store.viewsets import (CategoryViewSet, ProductViewSet)


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'clients', ClientViewSet)
router.register(r'testimonials', TestimonyViewSet)
router.register(r'store/categories', CategoryViewSet)
router.register(r'store/products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^cart', include([
        url(r'^$', ShoppingCartView.as_view(),
            name='list'),
        url(r'^/add$', AddProductToCartView.as_view(),
            name='add'),
        url(r'^/remove$', RemoveProductFromCartView.as_view(),
            name='remove'),
    ], namespace='cart')),
]