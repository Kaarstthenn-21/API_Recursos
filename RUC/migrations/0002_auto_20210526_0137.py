# Generated by Django 3.0.5 on 2021-05-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RUC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruc',
            name='rucEmpresa',
            field=models.IntegerField(max_length=11, unique=True, verbose_name='RUC'),
        ),
    ]