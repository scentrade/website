# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20150504_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='target',
            field=models.CharField(max_length=20, verbose_name='Mercado objetivo', choices=[(b'commercial', 'Comercial'), (b'home', 'Hogar')]),
        ),
    ]
