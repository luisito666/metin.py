# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='token_expirte',
            new_name='token_expire',
        ),
    ]
