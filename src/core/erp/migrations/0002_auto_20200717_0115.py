# Generated by Django 3.0.8 on 2020-07-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelTable(
            name='employee',
            table='empleado',
        ),
    ]