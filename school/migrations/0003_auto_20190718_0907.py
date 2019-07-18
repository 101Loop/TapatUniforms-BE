# Generated by Django 2.2.2 on 2019-07-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190717_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=1, max_length=100, verbose_name='Student ID'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('student_id', 'school')},
        ),
        migrations.RemoveField(
            model_name='student',
            name='id_no',
        ),
    ]
