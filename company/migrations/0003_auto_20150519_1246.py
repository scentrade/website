# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150504_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='testimony',
            options={'verbose_name': 'Testimonio', 'verbose_name_plural': 'Testimonios'},
        ),
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.URLField(default='', verbose_name='Link a la web del cliente'),
            preserve_default=False,
        ),
    ]
