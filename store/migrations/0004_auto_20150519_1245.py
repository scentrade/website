# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20150519_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_in_cop',
            field=models.PositiveIntegerField(default=0, help_text='En pesos Colombianos (COP)', verbose_name='Precio (COP)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_in_mx',
            field=models.PositiveIntegerField(default=0, help_text='En pesos Mexicanos', verbose_name='Precio (MX)'),
            preserve_default=False,
        ),
    ]
