# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20151130_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 21, 48, 30, 627989, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
