# Generated by Django 2.2.2 on 2019-07-17 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("outlet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("name", models.CharField(max_length=254, verbose_name="Buyer Name")),
                (
                    "mobile",
                    models.CharField(max_length=15, verbose_name="Buyer Mobile Number"),
                ),
                ("email", models.CharField(max_length=500, verbose_name="Buyer Email")),
                ("discount", models.IntegerField(verbose_name="Discount")),
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
            ],
            options={"verbose_name": "Order", "verbose_name_plural": "Orders"},
        ),
        migrations.CreateModel(
            name="Transaction",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Amount"
                    ),
                ),
                (
                    "mode",
                    models.CharField(max_length=254, verbose_name="Mode of Payment"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="order.Order",
                        verbose_name="Order",
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
            },
        ),
        migrations.CreateModel(
            name="SubOrder",
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
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="Quantity")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="order.Order",
                        verbose_name="Order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="outlet.OutletProduct",
                        verbose_name="Outlet Product",
                    ),
                ),
            ],
            options={"verbose_name": "SubOrder", "verbose_name_plural": "Sub Orders"},
        ),
        migrations.CreateModel(
            name="Discount",
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
                    "product_quantity",
                    models.IntegerField(verbose_name="Number of Items"),
                ),
                (
                    "discount_type",
                    models.CharField(
                        choices=[("P", "PERCENTAGE"), ("A", "AMOUNT"), ("O", "OTHER")],
                        default="A",
                        max_length=3,
                        verbose_name="Discount Type",
                    ),
                ),
                ("value", models.IntegerField(default=0, verbose_name="Value")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Discount", "verbose_name_plural": "Discounts"},
        ),
    ]
