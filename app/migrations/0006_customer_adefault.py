# Generated by Django 3.1.7 on 2021-04-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210326_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='adefault',
            field=models.CharField(default='No', max_length=5),
        ),
    ]
