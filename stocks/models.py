from django.db import models
from datetime import date


class Stock(models.Model):
  name      = models.CharField(max_length=10)
  symbol    = models.CharField(max_length=10)
  market    = models.CharField(max_length=5)
  curr      = models.CharField(max_length=255, default="HKD")
  

class StockRecord(models.Model):
  stock     = models.ForeignKey(Stock, on_delete=models.RESTRICT)
  date      = models.DateField(default=date.today)
  price     = models.DecimalField(max_digits=25, decimal_places=4)


class StockInOut(models.Model):
  stock     = models.ForeignKey(Stock, on_delete=models.RESTRICT)
  date      = models.DateField(default=date.today)
  price     = models.DecimalField(max_digits=25, decimal_places=4)
  unit     = models.DecimalField(max_digits=10, decimal_places=4)
