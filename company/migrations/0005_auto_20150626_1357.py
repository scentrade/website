# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_testimony_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='client_age',
            field=models.PositiveIntegerField(null=True, verbose_name='Edad del cliente', blank=True),
        ),
    ]
