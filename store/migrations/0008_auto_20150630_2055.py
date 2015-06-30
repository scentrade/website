# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20150630_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
        ),
    ]
