# Generated by Django 5.0.3 on 2024-03-24 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('location', models.CharField(max_length=100, verbose_name='Адрес')),
                ('working_hours', models.TimeField(verbose_name='Время работы')),
                ('expiration_date', models.DateField(verbose_name='Срок годности')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.enterprise')),
            ],
        ),
    ]
