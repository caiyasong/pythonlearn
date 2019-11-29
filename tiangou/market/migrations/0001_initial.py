# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-01 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(verbose_name='商品编号')),
                ('productimg', models.CharField(max_length=100, verbose_name='商品图片')),
                ('content', models.CharField(max_length=1000, verbose_name='商品内容')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商城价格')),
                ('marketprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('storenums', models.IntegerField(verbose_name='库存')),
                ('productnum', models.IntegerField(verbose_name='销量')),
            ],
            options={
                'db_table': 'tg_goods',
            },
        ),
    ]