# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='product',
            name='target',
            field=models.CharField(default='home', max_length=20, choices=[(b'commercial', 'Comercial'), (b'home', 'Hogar')]),
            preserve_default=False,
        ),
    ]
