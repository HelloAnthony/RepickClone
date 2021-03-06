# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featured', '0002_auto_20170907_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuecell',
            options={'ordering': ('issue_raw', 'position'), 'verbose_name': 'Issue cell', 'verbose_name_plural': 'Issue cells'},
        ),
        migrations.AlterModelOptions(
            name='issueraw',
            options={'ordering': ('issue', 'position'), 'verbose_name': 'Issue Raw', 'verbose_name_plural': 'Issue Raws'},
        ),
        migrations.AddField(
            model_name='issuecell',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Position'),
        ),
    ]
