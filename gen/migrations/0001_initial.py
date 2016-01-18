# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mu', models.DecimalField(max_digits=8, decimal_places=8)),
                ('sigma', models.DecimalField(max_digits=8, decimal_places=8)),
                ('name', models.DateTimeField(unique=True, max_length=24)),
            ],
        ),
    ]
