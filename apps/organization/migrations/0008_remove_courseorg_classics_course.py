# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-21 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_courseorg_classics_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='classics_course',
        ),
    ]
