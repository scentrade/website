# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('client_age', models.PositiveIntegerField(verbose_name='Edad del cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestimonyTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_occupation', models.CharField(max_length=100, verbose_name='Profesi\xf3n del cliente')),
                ('text', models.TextField(verbose_name='Testimonio')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='company.Testimony', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'company_testimony_translation',
                'db_tablespace': '',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(help_text='PNG de fondo transparente. 190px x 90px', upload_to=b'company/clients', verbose_name='Logo'),
        ),
        migrations.AlterUniqueTogether(
            name='testimonytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
