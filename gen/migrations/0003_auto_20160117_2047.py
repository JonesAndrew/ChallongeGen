# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0002_auto_20160117_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sigma',
            field=models.DecimalField(max_digits=32, decimal_places=32),
        ),
    ]
