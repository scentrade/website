# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20150626_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonytranslation',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Testimonio'),
        ),
    ]
