# Generated by Django 5.0 on 2024-01-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitantes',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
    ]
