from rest_framework import viewsets
from store.models import Category, Product
from store.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related().all()
    serializer_class = ProductSerializer
    filter_fields = ('target', 'category',)