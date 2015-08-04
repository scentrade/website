# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20150706_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='delivery_preference',
            field=models.CharField(default='in_store', max_length=50, choices=[(b'in_store', 'Recoger en la tienda'), (b'shipping_in_capital', 'Env\xedo en Bogot\xe1')]),
            preserve_default=False,
        ),
    ]
