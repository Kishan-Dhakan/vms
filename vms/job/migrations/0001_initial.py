# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-07 05:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator("^[(A-Z)|(a-z)|(\\s)|(\\')]+$")])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, validators=[django.core.validators.RegexValidator("^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)|(\\')]+$")])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
    ]
