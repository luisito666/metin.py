# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('varios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='top',
            name='guid_name',
            field=models.CharField(max_length=26, null=True),
        ),
    ]
