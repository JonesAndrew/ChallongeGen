# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0006_auto_20160117_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
