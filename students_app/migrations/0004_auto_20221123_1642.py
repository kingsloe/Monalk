# Generated by Django 2.2 on 2022-11-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0003_auto_20221123_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='debt',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
