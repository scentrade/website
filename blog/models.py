# encoding: utf-8
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, \
    ModificationDateTimeField
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
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


class Post(TranslatableModel):
    category = models.ForeignKey(
        Category,
        related_name='posts',
        verbose_name=_(u'Categoría')
    )
    box_bg = ThumbnailerImageField(
        upload_to='blog/posts',
        verbose_name=_(u'Imagen de fondo de la caja'),
        help_text=_(u'585 x 618px. Será recortada si no.')
    )
    featured_picture = ThumbnailerImageField(
        upload_to='blog/posts',
        verbose_name=_(u'Imagen destacada del post'),
        help_text=_(u'1280 x 512px. Será recortada si no.')
    )

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    translations = TranslatedFields(
        title=models.CharField(
            max_length=100,
            verbose_name=_(u'Título')
        ),
        content=RichTextField(
            verbose_name=_(u'Contenido')
        ),
        meta_description=models.TextField(
            max_length=160,
            verbose_name=_(u'Meta description (SEO)'),
            help_text=_(u'Máximo 160 caracteres')
        )
    )
    slug = AutoSlugField(
        populate_from='title'
    )

    class Meta:
        verbose_name = _(u'Post')
        verbose_name_plural = _(u'Posts')
        ordering = ('-created',)

    def __unicode__(self):
        return self.lazy_translation_getter('title', self.pk)

    def get_box_bg_cropped(self):
        """
        Returns the box bg with proper size
        """
        return make_absolute_url(
            get_thumbnailer(self.box_bg).get_thumbnail({
                'size': (585, 618), 'crop': True}).url)

    def get_featured_picture_cropped(self):
        """
        Returns the box bg with proper size
        """
        return make_absolute_url(
            get_thumbnailer(self.featured_picture).get_thumbnail({
                'size': (1280, 512), 'crop': True}).url)