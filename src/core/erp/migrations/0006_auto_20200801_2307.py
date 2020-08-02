# Generated by Django 3.0.8 on 2020-08-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20200801_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ManyToManyField(to='erp.Category'),
        ),
    ]
