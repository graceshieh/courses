# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161115_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='id',
        ),
        migrations.AlterField(
            model_name='description',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses.Course'),
        ),
    ]