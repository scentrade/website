# encoding: utf-8
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
from utils.url import make_absolute_url


class Client(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_(u'Nombre')
    )
    logo = ThumbnailerImageField(
        upload_to='company/clients',
        verbose_name=_(u'Logo'),
        help_text=_(u'PNG de fondo transparente. 190px x 90px')
    )
    url = models.URLField(
        verbose_name=_(u'Link a la web del cliente')
    )

    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')

    def __unicode__(self):
        return self.name

    def get_logo_cropped(self):
        """
        Returns the logo with proper size
        """
        return make_absolute_url(
            get_thumbnailer(self.logo).get_thumbnail({
                'size': (190, 90), 'crop': True}).url)


class Testimony(TranslatableModel):
    client_name = models.CharField(
        max_length=100,
        verbose_name=_(u'Nombre del cliente')
    )
    client_age = models.PositiveIntegerField(
        verbose_name=_(u'Edad del cliente'),
        null=True, blank=True
    )
    url = models.URLField(
        verbose_name=_(u'URL del cliente'),
        null=True, blank=True
    )
    translations = TranslatedFields(
        client_occupation=models.CharField(
            max_length=100,
            verbose_name=_(u'Profesión del cliente')
        ),
        text=RichTextField(
            verbose_name=_(u'Testimonio')
        )
    )

    class Meta:
        verbose_name = _(u'Testimonio')
        verbose_name_plural = _(u'Testimonios')

    def __unicode__(self):
        return self.client_name