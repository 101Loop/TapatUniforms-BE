# Generated by Django 2.2.2 on 2019-07-17 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outlet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('location', models.CharField(max_length=10, verbose_name='Storage Location')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('outlet_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outlet.OutletProduct', verbose_name='Outlet Product')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'unique_together': {('outlet_product', 'location')},
            },
        ),
    ]
