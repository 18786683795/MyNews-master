# Generated by Django 2.0.1 on 2020-03-13 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='发布日期', verbose_name='发布日期'),
        ),
    ]
