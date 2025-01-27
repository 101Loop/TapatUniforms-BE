# Generated by Django 2.2.2 on 2019-07-17 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Outlet",
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
                ("name", models.CharField(max_length=254, verbose_name="Name")),
                ("location", models.CharField(max_length=254, verbose_name="Location")),
                (
                    "short_name",
                    models.CharField(max_length=254, verbose_name="Short Name"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Outlet", "verbose_name_plural": "Outlets"},
        ),
        migrations.CreateModel(
            name="OutletProduct",
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
                    "price",
                    models.DecimalField(
                        decimal_places=3, max_digits=10, verbose_name="Price"
                    ),
                ),
                ("image", models.ImageField(upload_to="", verbose_name="Image")),
                (
                    "color",
                    models.CharField(
                        default="white", max_length=254, verbose_name="Color"
                    ),
                ),
                (
                    "color_code",
                    models.CharField(
                        default="#fff", max_length=254, verbose_name="Color Code"
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
                    "outlet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="outlet.Outlet",
                        verbose_name="Outlet",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.Product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Outlet Product",
                "verbose_name_plural": "Outlet Products",
                "unique_together": {("outlet", "product")},
            },
        ),
    ]
