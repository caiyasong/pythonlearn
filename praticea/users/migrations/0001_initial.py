# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-20 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('email', models.CharField(default='', max_length=50, verbose_name='邮箱')),
                ('avatar', models.ImageField(upload_to='uploads', verbose_name='头像')),
                ('is_active', models.BooleanField(default=0, verbose_name='激活状态')),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
