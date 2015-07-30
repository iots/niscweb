# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowEndAlive',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uuid', models.CharField(unique=True, max_length=32, blank=True, null=True)),
                ('mac_address', models.CharField(max_length=32, blank=True, null=True)),
                ('ip_address', models.CharField(max_length=15, blank=True, null=True)),
                ('product_id', models.CharField(max_length=32, blank=True, null=True)),
                ('os_version', models.CharField(max_length=32, blank=True, null=True)),
                ('kernel_version', models.CharField(max_length=32, blank=True, null=True)),
                ('cpu_model', models.CharField(max_length=64, blank=True, null=True)),
                ('bios_version', models.CharField(max_length=16)),
                ('graphics_model', models.CharField(max_length=128, blank=True, null=True)),
                ('graphics_driver_version', models.CharField(max_length=32, blank=True, null=True)),
                ('client_version', models.CharField(max_length=8, blank=True, null=True)),
                ('online_time', models.IntegerField(blank=True, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'show_end_alive',
                'managed': False,
            },
        ),
    ]
