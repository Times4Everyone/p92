# Generated by Django 3.1.3 on 2021-08-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210814_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
