# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20150630_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Comprador', 'verbose_name_plural': 'Compradores'},
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='order',
        ),
    ]
