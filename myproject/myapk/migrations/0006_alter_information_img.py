# Generated by Django 5.0.1 on 2024-02-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapk', '0005_alter_information_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
