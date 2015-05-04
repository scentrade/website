from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from store.models import Category, Product


class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category


class ProductSerializer(TranslatableModelSerializer):
    main_picture = ReadOnlyField(source='get_main_picture_cropped')
    html_name = ReadOnlyField(source='get_html_name')

    class Meta:
        model = Product


class CartProductSerializer(serializers.Serializer):
    """
    A serializer with an ID field.
    Will be used to add or remove a product to cart with django-carton
    """
    product_id = serializers.IntegerField()