# Generated by Django 2.2.2 on 2019-07-09 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, verbose_name='Category')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Image')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, verbose_name='Product')),
                ('sku', models.CharField(max_length=254, unique=True, verbose_name='SKU Code')),
                ('gender_type', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], default='M', max_length=254, verbose_name='Gender')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.CategoryMaster')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
        ),
    ]
