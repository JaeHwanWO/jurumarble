# Generated by Django 2.1.3 on 2019-05-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_data_dicenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='players',
            field=models.IntegerField(default=0),
        ),
    ]