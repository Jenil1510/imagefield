# Generated by Django 5.0.1 on 2024-02-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapk', '0008_alter_information_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='jenil_project/myproject/media/images/'),
        ),
    ]
