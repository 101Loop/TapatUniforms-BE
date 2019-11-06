# Generated by Django 2.2.2 on 2019-11-05 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("stock_order", "0011_auto_20191104_1558")]

    operations = [
        migrations.AlterField(
            model_name="box",
            name="indent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="stock_order.Indent"
            ),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="box",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="stock_order.Box"
            ),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="outlet.OutletSubProduct",
            ),
        ),
        migrations.AlterField(
            model_name="indentrequest",
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
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.Product"
            ),
        ),
    ]