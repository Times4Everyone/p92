# Generated by Django 3.1.3 on 2021-08-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210814_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recentlink',
            field=models.CharField(max_length=255, null=True),
        ),
    ]