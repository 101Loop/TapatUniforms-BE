# Generated by Django 2.2.2 on 2019-10-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20191023_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='school',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.TextField(max_length=254, verbose_name='Full Address'),
        ),
    ]
