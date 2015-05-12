# encoding: utf-8
from django import forms
from django.utils.translation import ugettext, get_language, ugettext_lazy as _
from djangular.forms import NgFormValidationMixin, NgForm, NgModelFormMixin
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin


class ContactForm(NgModelFormMixin,
                  NgFormValidationMixin,
                  Bootstrap3FormMixin,
                  NgForm,
                  forms.Form):
    """
    Website is contact form.

    Inheriting from NgModelFormMixin because of the need to be able to use
    scope_prefix.
    """
    name = forms.CharField(
        label=_(u'Nombre'),
        widget=forms.TextInput(attrs={'placeholder': _(u'Nombre')})
    )
    email = forms.EmailField(
        label=_(u'Correo electrónico'),
        widget=forms.EmailInput(attrs={'placeholder': _(u'Correo electrónico')})
    )
    comment = forms.CharField(
        label=_(u'Comentarios'),
        widget=forms.Textarea(attrs={'placeholder': _(u'Comentarios'), 'rows': 3})
    )