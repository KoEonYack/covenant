# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-11 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='realname',
        ),
    ]
