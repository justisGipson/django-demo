from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class Listings(models.Model):
    class SaleType(models.TextChoices):
        PICK_UP = "available for pickup"
        SHIP = "Available for shipping"

    class ConditionType(models.TextChoices):
        USED = "used"
        NEW = "New"

    class ProductType(models.TextChoices):
        BIKE = "Bike"
        PARTS = "Parts"
        OTHER = "Other"

    title = models.CharField(max_length=100)

    condition = models.CharField(
        max_length=50, choices=ConditionType.choices, default=ConditionType.USED
    )

    product_type = models.CharField(
        max_length=50, choices=ProductType.choices, default=ProductType.PARTS
    )

    sales_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.SHIP
    )

    price = models.FloatField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    main_photo = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField(blank=True)
    list_date = models.DateTimeField(default=now)
    contact_email = models.CharField(max_length=50)

    def __str__(self):
        return self.title
