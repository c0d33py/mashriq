# Generated by Django 3.0.2 on 2020-04-17 13:05

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200417_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='(optional)', null=True, upload_to=news.models.article_path),
        ),
    ]