# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0003_auto_20160117_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='mu',
            field=models.DecimalField(max_digits=64, decimal_places=64),
        ),
        migrations.AlterField(
            model_name='player',
            name='sigma',
            field=models.DecimalField(max_digits=64, decimal_places=64),
        ),
    ]
