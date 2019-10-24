# Generated by Django 2.2.2 on 2019-10-23 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0002_warehouse"),
        ("school", "0004_auto_20190718_1241"),
    ]

    operations = [
        migrations.AddField(
            model_name="school",
            name="city",
            field=models.ForeignKey(
                help_text="School's City",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="location.City",
                verbose_name="City",
            ),
        ),
        migrations.AddField(
            model_name="school",
            name="state",
            field=models.ForeignKey(
                help_text="School's State",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="location.State",
                verbose_name="State",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("B", "Both")],
                max_length=1,
                verbose_name="Gender",
            ),
        ),
    ]
