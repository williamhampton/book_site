# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 23:25
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0002_books'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='books',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]