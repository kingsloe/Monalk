# Generated by Django 2.2 on 2023-03-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0005_auto_20221123_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='termly_debt',
            field=models.FloatField(blank=True, null=True),
        ),
    ]