# Generated by Django 2.2.2 on 2019-07-20 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("outlet", "0002_auto_20190718_1135"),
    ]

    operations = [
        migrations.RemoveField(model_name="outletproduct", name="display_stock"),
        migrations.RemoveField(model_name="outletproduct", name="price"),
        migrations.RemoveField(model_name="outletproduct", name="size"),
        migrations.RemoveField(model_name="outletproduct", name="warehouse_stock"),
        migrations.CreateModel(
            name="OutletSubProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Create Date/Time"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date/Time Modified"
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("24", "24"),
                            ("26", "26"),
                            ("28", "28"),
                            ("30", "30"),
                            ("32", "32"),
                            ("34", "34"),
                            ("36", "36"),
                            ("38", "38"),
                            ("40", "40"),
                        ],
                        default="24",
                        max_length=4,
                        verbose_name="Size",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=3, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "warehouse_stock",
                    models.IntegerField(default=0, verbose_name="Warehouse Stock"),
                ),
                (
                    "display_stock",
                    models.IntegerField(default=0, verbose_name="Display Stock"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "outlet_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="outlet.OutletProduct",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Outlet SubProducts",
                "verbose_name": "Outlet SubProduct",
            },
        ),
    ]
