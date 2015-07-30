# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowPushMessage',
            fields=[
                ('id', models.AutoField(db_column='Id', serialize=False, primary_key=True)),
                ('raw_data_id', models.IntegerField(blank=True, null=True)),
                ('sent_message', models.TextField()),
                ('sent_url', models.TextField(blank=True, null=True)),
                ('sent_number', models.IntegerField(blank=True, null=True)),
                ('recv_number', models.IntegerField(blank=True, null=True)),
                ('open_number', models.IntegerField(blank=True, null=True)),
                ('sent_time', models.IntegerField(blank=True, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'show_push_message',
            },
        ),
    ]
