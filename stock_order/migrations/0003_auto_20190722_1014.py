# Generated by Django 2.2.2 on 2019-07-22 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_order', '0002_auto_20190720_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxitem',
            name='item_in_shelf',
        ),
        migrations.AlterField(
            model_name='boxitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outlet.OutletSubProduct'),
        ),
    ]