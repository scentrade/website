# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='', help_text='1280 x 512px. Ser\xe1 recortada si no.', verbose_name='Imagen destacada del post', upload_to=b'blog/posts'),
            preserve_default=False,
        ),
    ]
