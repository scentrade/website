# encoding: utf-8
from carton.cart import Cart
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext, ugettext_lazy as _
from rest_framework import generics, status
from rest_framework.response import Response
from store.models import Product
from store.serializers import CartProductSerializer


class ShoppingCartView(generics.GenericAPIView):
    """
    Return the list of the products in the cart.
    """
    def get(self, request):
        cart = Cart(request.session)
        products = []
        for item in cart.items:
            products.append({
                # TODO get in right language
                'name': item.product.get_html_name(),
                'price': item.price,
                'quantity': item.quantity,
                'id': item.product.id
            })
        return Response({
            'products': products,
            'total': cart.total
        }, status=status.HTTP_200_OK)


class AddProductToCartView(generics.GenericAPIView):
    """
    Add a product to the cart.
    Send a valid product_id
    """
    serializer_class = CartProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = Cart(request.session)
        product = get_object_or_404(Product, id=serializer.data['product_id'])
        cart.add(product, price=product.price)

        response_data = {
            'detail': 'Product was added to cart.'
        }
        response_status = status.HTTP_201_CREATED

        return Response(response_data, status=response_status)


class UpdateQuantityCartView(generics.GenericAPIView):
    """
    Add a product to the cart.
    Send a valid product_id
    """
    serializer_class = CartProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = Cart(request.session)
        product = get_object_or_404(Product, id=serializer.data['product_id'])
        cart.set_quantity(product, quantity=serializer.data['product_quantity'])

        response_data = {
            'detail': 'Product was updated.'
        }
        response_status = status.HTTP_201_CREATED

        return Response(response_data, status=response_status)


class RemoveProductFromCartView(generics.GenericAPIView):
    """
    Remove a product from the cart.
    Send a valid product_id
    """
    serializer_class = CartProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = Cart(request.session)
        product = get_object_or_404(Product, id=serializer.data['product_id'])
        cart.remove(product)

        response_data = {
            'detail': 'Product was removed from cart.'
        }
        response_status = status.HTTP_200_OK

        return Response(response_data, status=response_status)