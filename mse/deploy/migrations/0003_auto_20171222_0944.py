# Generated by Django 2.0 on 2017-12-22 09:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_auto_20171222_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2017, 12, 22, 9, 44, 27, 909609, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 44, 27, 909639, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='server',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2017, 12, 22, 9, 44, 27, 908914, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='server',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 44, 27, 908955, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='version',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2017, 12, 22, 9, 44, 27, 896466, tzinfo=utc), verbose_name='date created'),
        ),
    ]
