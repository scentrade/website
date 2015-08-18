# encoding: utf-8
from adminsortable.models import Sortable
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext, ugettext_lazy as _
from django_extensions.db.fields.json import JSONField
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
from store.choices import PRODUCT_TARGET
from utils.url import make_absolute_url


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=100,
            verbose_name=_(u'Nombre')
        )
    )
    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')

    def __unicode__(self):
        # TODO check why safe translation returns always the id
        # return self.safe_translation_getter('name', str(self.pk))
        return self.lazy_translation_getter('name', str(self.pk))


class Product(TranslatableModel, Sortable):
    category = models.ForeignKey(
        Category,
        related_name='products',
        verbose_name=_(u'Categoría')
    )
    target = models.CharField(
        max_length=20,
        choices=PRODUCT_TARGET,
        verbose_name=_(u'Mercado objetivo')
    )
    main_picture = ThumbnailerImageField(
        upload_to='store/products',
        verbose_name=_(u'Fotografía del producto'),
        help_text=_(u'500px x 500px, será recortada si no.')
    )
    price_in_cop = models.PositiveIntegerField(
        verbose_name=_(u'Precio (COP)'),
        help_text=_(u'En pesos Colombianos (COP)')
    )
    price_in_mx = models.PositiveIntegerField(
        verbose_name=_(u'Precio (MX)'),
        help_text=_(u'En pesos Mexicanos')
    )
    translations = TranslatedFields(
        name=models.CharField(
            max_length=100,
            verbose_name=_(u'Nombre')
        ),
        description=models.TextField(
            verbose_name=_(u'Descripción')
        )
    )
    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta(Sortable.Meta):
        verbose_name = _(u'Producto')
        verbose_name_plural = _(u'Productos')

    def __unicode__(self):
        return self.safe_translation_getter('name', str(self.pk))

    def get_html_name(self):
        """
        Return html formatted name, works with product listing
        and shopping cart.
        """
        translated_name = self.lazy_translation_getter('name')
        return translated_name\
            .replace('[', '<span>')\
            .replace(']', '</span>')

    def get_name_cleaned(self):
        translated_name = self.lazy_translation_getter('name')
        return translated_name\
            .replace('[', '')\
            .replace(']', '')

    def get_main_picture_cropped(self):
        """
        Returns the main picture with proper size
        """
        return make_absolute_url(
            get_thumbnailer(self.main_picture).get_thumbnail({
                'size': (500, 500), 'crop': True}).url)

    @property
    def price(self):
        return self.price_in_cop


class Buyer(models.Model):
    first_name = models.CharField(
        max_length=200
    )
    last_name = models.CharField(
        max_length=200
    )
    email = models.EmailField(

    )
    city = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=100
    )
    phone = models.BigIntegerField()
    delivery_preference = models.CharField(
        max_length=50,
        choices=[
            ('in_store', u'Recoger en la tienda'),
            ('shipping_in_capital', u'Envío en Bogotá'),
            # ('shipping_out_bogota', u'Envío fuera de Bogotá'),
        ]
    )

    class Meta:
        verbose_name = _(u'Comprador')
        verbose_name_plural = _(u'Compradores')

    def __unicode__(self):
        return u'{0} {1}'.format(
            self.first_name,
            self.last_name
        )

    def get_full_name(self):
        return u'{first} {last}'.format(
            first=self.first_name,
            last=self.last_name
        )


class Purchase(models.Model):
    buyer = models.ForeignKey(
        Buyer, related_name='purchases'
    )
    cart = JSONField()

    class Meta:
        verbose_name = _(u'Compra')
        verbose_name_plural = _(u'Compras')

    def __unicode__(self):
        return u'{0}'.format(self.buyer)