from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.nationality}"


class Mobile(models.Model):
    STATUS = (
        (False, '-'),
        (True, '+'),
    )

    brand_id = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(null=True)
    color = models.CharField(max_length=100, null=True)
    screen_size = models.FloatField(null=True)
    status = models.BooleanField(choices=STATUS, null=True)
    builder_country = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.model}"
