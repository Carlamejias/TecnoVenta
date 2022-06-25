# Generated by Django 4.0.5 on 2022-06-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca Producto')),
                ('precio', models.IntegerField()),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo Producto')),
                ('categoria', models.CharField(max_length=30, verbose_name='Categoria')),
                ('peso', models.CharField(max_length=30, verbose_name='Peso')),
            ],
        ),
    ]
