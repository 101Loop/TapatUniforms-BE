# Generated by Django 2.2.2 on 2019-07-22 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0003_auto_20190720_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='outletproduct',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Outlet Product Name'),
            preserve_default=False,
        ),
    ]
