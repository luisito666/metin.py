# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provedor', models.CharField(max_length=30)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=3)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.IntegerField()),
                ('name', models.CharField(max_length=26)),
                ('level', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('ranking', models.SmallIntegerField(null=True, blank=True)),
            ],
        ),
    ]
