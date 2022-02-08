# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0003_auto_20170325_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='alipay',
            field=models.URLField(max_length=255, null=True, verbose_name='Alipay URL'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='weibo_url',
            field=models.URLField(max_length=255, null=True, verbose_name='Weibo URL'),
        ),
    ]
