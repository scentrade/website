# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150519_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='url',
            field=models.URLField(null=True, verbose_name='URL del cliente', blank=True),
        ),
    ]
