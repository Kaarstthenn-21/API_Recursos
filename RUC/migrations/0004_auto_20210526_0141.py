# Generated by Django 3.0.5 on 2021-05-26 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RUC', '0003_auto_20210526_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruc',
            old_name='rutaRuc',
            new_name='rutaRUC',
        ),
    ]