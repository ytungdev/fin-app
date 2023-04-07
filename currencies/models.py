from django.db import models
from datetime import date


class CurrencyRecord(models.Model):
  curr   = models.CharField(max_length=5)
  date    = models.DateField(default=date.today)
  rate   = models.DecimalField(max_digits=25, decimal_places=4)