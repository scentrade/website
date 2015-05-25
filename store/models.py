# encoding: utf-8
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext, ugettext_lazy as _
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


class Product(TranslatableModel):
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

    class Meta:
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

    def get_main_picture_cropped(self):
        """
        Returns the main picture with proper size
        """
        return make_absolute_url(
            get_thumbnailer(self.main_picture).get_thumbnail({
                'size': (500, 500), 'crop': True}).url)