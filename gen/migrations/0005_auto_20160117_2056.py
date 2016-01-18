# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0004_auto_20160117_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='mu',
            field=models.DecimalField(max_digits=52, decimal_places=48),
        ),
        migrations.AlterField(
            model_name='player',
            name='sigma',
            field=models.DecimalField(max_digits=52, decimal_places=48),
        ),
    ]
