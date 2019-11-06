# Generated by Django 2.2.2 on 2019-11-04 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("stock_order", "0010_auto_20191104_1535")]

    operations = [
        migrations.AlterField(
            model_name="indent",
            name="outlet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="outlet.Outlet",
                verbose_name="Outlet",
            ),
        ),
        migrations.AlterField(
            model_name="indentrequest",
            name="outlet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="outlet.Outlet",
                verbose_name="Outlet",
            ),
        ),
    ]