# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zip', models.IntegerField()),
                ('diagnosis', models.TextField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
