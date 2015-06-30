from rest_framework import viewsets
from store.models import Category, Product, Buyer, Purchase
from store.serializers import CategorySerializer, ProductSerializer, \
    BuyerSerializer, PurchaseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related().all()
    serializer_class = ProductSerializer
    filter_fields = ('target', 'category',)


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.select_related().all()
    serializer_class = BuyerSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.select_related().all()
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        # Because in the serializer I have company with read_only = True
        if self.request.data.get('buyer', None):
            buyer = Buyer.objects.get(pk=self.request.data['buyer'])
            serializer.save(buyer=buyer)
        else:
            serializer.save()