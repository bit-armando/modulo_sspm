# Generated by Django 5.0 on 2023-12-28 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_visitantes_fecha_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitantes',
            name='fecha_entrada',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 18, 57, 2, 207771, tzinfo=datetime.timezone.utc)),
        ),
    ]
