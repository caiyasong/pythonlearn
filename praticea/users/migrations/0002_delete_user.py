# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-20 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
