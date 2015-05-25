# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20150519_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttranslation',
            name='description',
            field=models.TextField(default='', verbose_name='Descripci\xf3n'),
            preserve_default=False,
        ),
    ]
