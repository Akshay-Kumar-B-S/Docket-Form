from django.db import models

# Create your models here.

from django.db import models

class Docket(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours_worked = models.FloatField()
    rate_per_hour = models.FloatField()
    supplier_name = models.CharField(max_length=100)
    purchase_order = models.CharField(max_length=100)

    url = models.URLField()

    def __str__(self):
        return self.name

