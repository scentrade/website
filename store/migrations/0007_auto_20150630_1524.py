# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart', django_extensions.db.fields.json.JSONField()),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Comprador', 'verbose_name_plural': 'Compradores'},
        ),
        migrations.AddField(
            model_name='purchase',
            name='buyer',
            field=models.ForeignKey(related_name='purchases', to='store.Buyer'),
        ),
    ]
