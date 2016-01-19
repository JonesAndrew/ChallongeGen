# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0008_auto_20160118_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tournaments', models.ManyToManyField(to='gen.Tournament')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
