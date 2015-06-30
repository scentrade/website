# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20150630_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='buyer',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
        ),
    ]
