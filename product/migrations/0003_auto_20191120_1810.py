# Generated by Django 2.2.2 on 2019-11-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191024_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymaster',
            name='name',
            field=models.CharField(max_length=254, unique=True, verbose_name='Category'),
        ),
    ]