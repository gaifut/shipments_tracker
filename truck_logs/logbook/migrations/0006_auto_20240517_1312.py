# Generated by Django 3.2.16 on 2024-05-17 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0005_auto_20240517_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='overheating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments_overheating', to='logbook.truck'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='overload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments_overload', to='logbook.truck'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='techincal_check',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments_techincal_check', to='logbook.truck'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='unplanend_repairs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments_unplanend_repairs', to='logbook.truck'),
        ),
        migrations.AddField(
            model_name='truck',
            name='overheating',
            field=models.DateField(blank=True, null=True, verbose_name='Перегрев'),
        ),
        migrations.AddField(
            model_name='truck',
            name='overload',
            field=models.DateField(blank=True, null=True, verbose_name='Перегруз'),
        ),
        migrations.AddField(
            model_name='truck',
            name='techincal_check',
            field=models.DateField(blank=True, null=True, verbose_name='Техосмотр'),
        ),
        migrations.AddField(
            model_name='truck',
            name='unplanend_repairs',
            field=models.DateField(blank=True, null=True, verbose_name='СТО'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_no',
            field=models.CharField(max_length=15, verbose_name='Номер грузовика'),
        ),
    ]