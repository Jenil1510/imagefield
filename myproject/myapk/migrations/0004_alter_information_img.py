# Generated by Django 5.0.1 on 2024-02-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapk', '0003_information_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
