# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
