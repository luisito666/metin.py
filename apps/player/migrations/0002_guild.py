# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=12)),
                ('sp', models.SmallIntegerField()),
                ('master', models.IntegerField()),
                ('level', models.IntegerField(null=True, blank=True)),
                ('exp', models.IntegerField(null=True, blank=True)),
                ('skill_point', models.IntegerField()),
                ('skill', models.TextField(null=True, blank=True)),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('ladder_point', models.IntegerField()),
                ('gold', models.IntegerField()),
            ],
            options={
                'db_table': 'guild',
                'managed': False,
            },
        ),
    ]
