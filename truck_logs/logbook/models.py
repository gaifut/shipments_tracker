from django.db import models
from django.contrib.auth.models import User

from truck_logs.constants import TRUCK_CHAR_MAX_LENGTH, CHARFIELD_MAX_LENGTH
# from users.models import User


class Truck(models.Model):
    truck_no = models.CharField(
        max_length=TRUCK_CHAR_MAX_LENGTH,
        verbose_name='Номер грузовика',
    )
    techincal_check = models.DateField(
        blank=True,
        null=True,
        verbose_name='Техосмотр',
    )
    unplanend_repairs = models.DateField(
        blank=True,
        null=True,
        verbose_name='СТО',
    )
    # Перегруз я не понял какой именно: из авто в авто груз или в значении много груза.
    overload = models.DateField(
        blank=True,
        null=True,
        verbose_name='Перегруз',
    )
    overheating = models.DateField(
        blank=True,
        null=True,
        verbose_name='Перегрев',
    )

    def __str__(self) -> str:
        return self.truck_no


class Shipment(models.Model):
    person_responsible = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shipments',
    )
    truck_no = models.ForeignKey(
        Truck, on_delete=models.CASCADE, related_name='shipments',
    )
    departure_point = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Пункт отправления',
    )
    destination_point = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        verbose_name='Пункт назначения',
    )
    departure_date = models.DateField(
        verbose_name='Дата отправления',
    )
    arrival_date = models.DateField(
        verbose_name='Дата прибытия',
    )
    truck_actual_arrival_time_departure_point = models.DateField(
        blank=True,
        null=True,
        verbose_name='Вермя факт прибытия авто в пункт отправления',
    )
    truck_actual_departure_time_departure_point = models.DateField(
        blank=True,
        null=True,
        verbose_name='Вермя факт отбытия авто из пункта отправления',
    )
    truck_actual_arrival_time_destination_point = models.DateField(
        blank=True,
        null=True,
        verbose_name='Вермя факт прибытия авто в пункт назначения',
    )
    truck_actual_departure_time_destination_point = models.DateField(
        blank=True,
        null=True,
        verbose_name='Вермя факт отбытия авто из пункта назначения',
    )
    techincal_check = models.ForeignKey(
        Truck,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='shipments_techincal_check',
    )
    unplanend_repairs = models.ForeignKey(
        Truck,
        on_delete=models.CASCADE,
        related_name='shipments_unplanend_repairs',
        null=True,
        blank=True,
    )
    overload = models.ForeignKey(
        Truck,
        on_delete=models.CASCADE,
        related_name='shipments_overload',
        null=True,
        blank=True,
    )
    overheating = models.ForeignKey(
        Truck,
        on_delete=models.CASCADE,
        related_name='shipments_overheating',
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f'Из {self.departure_point} в {self.destination_point}'
