# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20170906_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-when_created',), 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='item',
            name='in_trend',
            field=models.BooleanField(default=True, verbose_name='Trend'),
        ),
        migrations.AlterField(
            model_name='item',
            name='related_items',
            field=models.ManyToManyField(blank=True, through='catalogue.RelatedItems', to='catalogue.Item', verbose_name='Related itemd'),
        ),
        migrations.AlterField(
            model_name='relateditems',
            name='recommendation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Item', verbose_name='Recomendation Items'),
        ),
    ]
