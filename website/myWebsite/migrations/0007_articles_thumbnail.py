# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import myWebsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebsite', '0006_auto_20170122_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumbnail',
            field=models.FileField(default=datetime.datetime(2017, 1, 21, 20, 2, 37, 774377, tzinfo=utc), upload_to=myWebsite.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
