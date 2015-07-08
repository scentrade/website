# encoding: utf-8
from carton.cart import Cart
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.translation import ugettext, ugettext_lazy as _
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from store.models import Product, Purchase
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


class PaymentEmailView(APIView):
    """
    The API view that sends an email each time a user make a payment
    """
    def post(self, request):
        response_data = {}
        response_status = None

        data = request.data
        purchase_id = request.data.get('purchase', None)

        if purchase_id:
            purchase = Purchase.objects.get(id=int(purchase_id))
            from_email = u'{name} <{email}>'.format(
                name=u'Pagos scentrade',
                email=u'pagos@scentrade.co'
            )
            msg = EmailMultiAlternatives(
                subject=_(u'[scentrade/pagos] Nuevo pago de {name}').format(
                    name=purchase.buyer.first_name
                ),
                body=render_to_string(
                    'store/emails/payment.txt',
                    {'purchase': purchase}),
                from_email=from_email,
                to=[
                    settings.PAYMENT_EMAIL_SEND_TO
                ],
                headers={
                    'Reply-To': from_email
                }
            )
            msg.send()
            response_data['detail'] = u'Email sent'
            response_status = status.HTTP_200_OK
        else:
            response_data['detail'] = u'Purchase ID not sent'
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=response_status)