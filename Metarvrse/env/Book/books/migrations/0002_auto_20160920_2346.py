# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-20 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='isbn_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
