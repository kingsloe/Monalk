# Generated by Django 2.2 on 2022-10-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(default='school', max_length=20, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
