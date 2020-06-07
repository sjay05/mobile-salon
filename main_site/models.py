from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shop_name = models.CharField(max_length=500, unique=True)
    shop_description = models.CharField(max_length=2000)
    shop_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name

STATUSES = (
    ('PENDING', 'PENDING'),
    ('FINISHED', 'FINISHED')
)

class Booking(models.Model):
    booker = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    status = models.CharField(choices=STATUSES, max_length=500)
    phone_number = models.CharField(max_length=50)