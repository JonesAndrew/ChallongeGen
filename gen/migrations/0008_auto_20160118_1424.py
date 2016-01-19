# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0007_auto_20160118_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='losses',
            new_name='Glosses',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='wins',
            new_name='Gwins',
        ),
        migrations.AddField(
            model_name='player',
            name='Slosses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='Swins',
            field=models.IntegerField(default=0),
        ),
    ]
