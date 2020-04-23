# Generated by Django 3.0.2 on 2020-04-18 22:34

import datetime
from django.db import migrations
from django.utils.timezone import utc
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200417_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=datetime.datetime(2020, 4, 18, 22, 34, 46, 324407, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
