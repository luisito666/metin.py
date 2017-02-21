# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('publicado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-creado'],
                'verbose_name': 'Entrada del Blog',
                'verbose_name_plural': 'Entradas del blog',
            },
        ),
    ]
