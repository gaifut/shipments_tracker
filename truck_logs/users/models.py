# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.validators import UnicodeUsernameValidator

# from truck_logs.constants import CHARFIELD_MAX_LENGTH


# class User(AbstractUser):
#     """Модель пользователя (логиста)."""
#     username = models.CharField(
#         verbose_name='Имя пользователя',
#         max_length=CHARFIELD_MAX_LENGTH,
#         unique=True,
#         validators=([UnicodeUsernameValidator()])
#     )
#     password = models.CharField(
#         max_length=CHARFIELD_MAX_LENGTH,
#         verbose_name='Пароль'
#     )
#     email = models.EmailField(
#         verbose_name='Адрес электронной почты',
#         unique=True
#     )
#     first_name = models.CharField(
#         max_length=CHARFIELD_MAX_LENGTH,
#         verbose_name='Имя'
#     )
#     last_name = models.CharField(
#         max_length=CHARFIELD_MAX_LENGTH,
#         verbose_name='Фамилия'
#     )

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

#     def __str__(self):
#         return self.username