# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sigma',
            field=models.DecimalField(max_digits=16, decimal_places=16),
        ),
    ]
