# Generated by Django 3.2.16 on 2024-05-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_point', models.CharField(max_length=150, verbose_name='Пункт отправления')),
                ('destination_point', models.CharField(max_length=150, verbose_name='Пункт доставки')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_no', models.CharField(max_length=15, verbose_name='номер грузовика')),
            ],
        ),
    ]