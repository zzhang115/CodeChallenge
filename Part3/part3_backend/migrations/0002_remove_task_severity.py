# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part3_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='severity',
        ),
    ]