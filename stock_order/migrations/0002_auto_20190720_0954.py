# Generated by Django 2.2.2 on 2019-07-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outlet.OutletProduct'),
        ),
    ]
