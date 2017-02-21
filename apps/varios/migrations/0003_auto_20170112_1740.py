# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('varios', '0002_top_guid_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='top',
            old_name='guid_name',
            new_name='guild_name',
        ),
    ]
