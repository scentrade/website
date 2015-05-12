# encoding: utf-8
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext, ugettext_lazy as _
from rest_framework import generics, status
from rest_framework.response import Response
from ng_app.forms import ContactForm


class ContactFormView(generics.GenericAPIView):
    """
    The API view which process the Contact form
    """
    def post(self, request):
        response_data = {}
        response_status = None

        contact_form = ContactForm(data=request.data)
        if contact_form.is_valid():
            from_email = '{name} <{email}>'.format(
                name=contact_form.cleaned_data['name'],
                email=contact_form.cleaned_data['email']
            )
            msg = EmailMultiAlternatives(
                subject=_(u'[scentrade/contacto] Nuevo mensaje de {name}').format(
                    name=contact_form.cleaned_data['name']
                ),
                body=render_to_string(
                    'ng_app/emails/contact.txt',
                    request.data),
                from_email=from_email,
                to=[
                    settings.CONTACT_FORM_SEND_TO
                ],
                headers={
                    'Reply-To': from_email
                }
            )
            msg.send()
            response_data['detail'] = _(
                u'Gracias por ponerte en contacto con nosotros, '
                u'tu mensaje ha sido enviado con éxito, te responderemos '
                u'tan pronto como sea posible.')
            response_status = status.HTTP_200_OK
        else:
            response_data['form_errors'] = contact_form.errors
            response_data['non_field_errors'] = contact_form.non_field_errors()
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(response_data, status=response_status)