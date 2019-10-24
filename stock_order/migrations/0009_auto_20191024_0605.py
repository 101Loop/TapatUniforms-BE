# Generated by Django 2.2.2 on 2019-10-24 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("stock_order", "0008_auto_20191024_0548")]

    operations = [
        migrations.RemoveField(model_name="indent", name="name"),
        migrations.RemoveField(model_name="indent", name="received_on"),
        migrations.AddField(
            model_name="indent",
            name="indent_name",
            field=models.ForeignKey(
                help_text="Name of the requested Indent",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stock_order.IndentRequest",
                verbose_name="Indent Name",
            ),
        ),
        migrations.AddField(
            model_name="indentrequest",
            name="received_on",
            field=models.DateTimeField(
                blank=True,
                help_text="To update the admin, when the order is received",
                null=True,
                verbose_name="Indent Received On",
            ),
        ),
        migrations.AddField(
            model_name="indentrequest",
            name="requested_on",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Indent Requested On"
            ),
        ),
    ]
