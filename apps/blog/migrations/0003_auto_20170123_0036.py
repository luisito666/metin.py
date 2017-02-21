# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170122_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='body',
            new_name='cuerpo',
        ),
    ]
