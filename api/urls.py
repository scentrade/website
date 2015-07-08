from django.conf.urls import *
from rest_framework import routers
from api.views import ContactFormView, FreeTrialFormView
from company.viewsets import (ClientViewSet, TestimonyViewSet)
from store.views import (AddProductToCartView, RemoveProductFromCartView,
                         ShoppingCartView, UpdateQuantityCartView,
                         PaymentEmailView)
from store.viewsets import (CategoryViewSet, ProductViewSet, BuyerViewSet,
                            PurchaseViewSet)
from blog.viewsets import (CategoryViewSet as BlogCategoryViewSet, PostViewSet)


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'clients', ClientViewSet)
router.register(r'testimonials', TestimonyViewSet)
router.register(r'store/categories', CategoryViewSet)
router.register(r'store/products', ProductViewSet)
router.register(r'store/buyers', BuyerViewSet)
router.register(r'store/purchases', PurchaseViewSet)
router.register(r'blog/categories', BlogCategoryViewSet)
router.register(r'blog/posts', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^cart', include([
        url(r'^$', ShoppingCartView.as_view(),
            name='list'),
        url(r'^/add$', AddProductToCartView.as_view(),
            name='add'),
        url(r'^/update$', UpdateQuantityCartView.as_view(),
            name='update'),
        url(r'^/remove$', RemoveProductFromCartView.as_view(),
            name='remove'),
    ], namespace='cart')),
    url(r'^contact$', ContactFormView.as_view(),
        name='contact'),
    url(r'^free-trial$', FreeTrialFormView.as_view(),
        name='free-trial'),
    url(r'^payment-email$', PaymentEmailView.as_view(),
        name='payment-email'),
]