# Generated by Django 2.2 on 2023-03-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0008_auto_20230309_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='cl',
            field=models.CharField(choices=[('F & B', 'F & B'), ('P.S.', 'P.S.'), ('K.S.A.', 'K.S.A.'), ('K.S.B.', 'K.S.B.'), ('K.S.C.', 'K.S.C.'), ('L.S.A.', 'L.S.A.'), ('L.S.B.', 'L.S.B.'), ('L.S.C.', 'L.S.C.')], max_length=10, null=True),
        ),
    ]
