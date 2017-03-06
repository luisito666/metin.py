# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(unique=True, max_length=30)),
                ('password', models.CharField(max_length=45)),
                ('real_name', models.CharField(max_length=16, null=True, blank=True)),
                ('social_id', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=64)),
                ('phone1', models.CharField(max_length=16, null=True, blank=True)),
                ('phone2', models.CharField(max_length=16, null=True, blank=True)),
                ('address', models.CharField(max_length=128, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=7, null=True, blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('question1', models.CharField(max_length=48, null=True, blank=True)),
                ('answer1', models.CharField(max_length=48, null=True, blank=True)),
                ('question2', models.CharField(max_length=48, null=True, blank=True)),
                ('answer2', models.CharField(max_length=48, null=True, blank=True)),
                ('is_testor', models.IntegerField(default=0)),
                ('status', models.CharField(default='OK', max_length=8)),
                ('securitycode', models.CharField(max_length=192, null=True, blank=True)),
                ('newsletter', models.IntegerField(null=True, blank=True)),
                ('empire', models.IntegerField(default=0)),
                ('name_checked', models.IntegerField(default=0)),
                ('availdt', models.DateTimeField(default='2009-01-01T00:00:00', db_column='availDt')),
                ('mileage', models.IntegerField(default=0)),
                ('coins', models.IntegerField(default=0)),
                ('gold_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('silver_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('safebox_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('autoloot_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('fish_mind_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('marriage_fast_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('money_drop_rate_expire', models.DateTimeField(default='2020-01-01T00:00:00')),
                ('ttl_cash', models.IntegerField(default=0)),
                ('ttl_mileage', models.IntegerField(default=0)),
                ('channel_company', models.CharField(max_length=30)),
                ('rang', models.IntegerField(null=True, blank=True)),
                ('last_play', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastvote', models.DateTimeField(default=django.utils.timezone.now)),
                ('day_of_vote', models.DateTimeField(default=django.utils.timezone.now)),
                ('cash', models.IntegerField(default=0)),
                ('web_admin', models.IntegerField(default=0)),
                ('web_ip', models.CharField(default=0, max_length=15)),
                ('web_aktiviert', models.CharField(max_length=32)),
                ('drs', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=256, null=True, blank=True)),
                ('web', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=0)),
                ('codigo_referido', models.CharField(max_length=32)),
                ('referido', models.CharField(max_length=32)),
                ('verificacion', models.CharField(default=0, max_length=32, db_column='Verificacion')),
                ('a_points', models.IntegerField(default=0)),
                ('votecoins', models.IntegerField(default=0)),
                ('token_expirte', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
    ]
