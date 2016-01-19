# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0009_tournament_tournamentlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='safe',
            field=models.DecimalField(default=0, max_digits=52, decimal_places=48),
            preserve_default=False,
        ),
    ]
