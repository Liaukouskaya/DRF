from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=65)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = {
        (1, 'Sedan'),
        (2, 'Universal'),
        (3, 'Hatchback'),
    }
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
