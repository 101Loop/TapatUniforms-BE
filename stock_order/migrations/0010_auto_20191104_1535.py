# Generated by Django 2.2.2 on 2019-11-04 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("outlet", "0005_auto_20191103_1540"),
        ("stock_order", "0009_auto_20191024_0605"),
    ]

    operations = [
        migrations.RemoveField(model_name="indent", name="school"),
        migrations.RemoveField(model_name="indentrequest", name="school"),
        migrations.AddField(
            model_name="indent",
            name="outlet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="outlet.Outlet",
                verbose_name="School",
            ),
        ),
        migrations.AddField(
            model_name="indentrequest",
            name="outlet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="outlet.Outlet",
                verbose_name="School",
            ),
        ),
    ]
