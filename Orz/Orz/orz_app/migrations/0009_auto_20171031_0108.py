# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orz_app', '0008_article_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_name',
            field=models.CharField(max_length=64),
        ),
    ]
