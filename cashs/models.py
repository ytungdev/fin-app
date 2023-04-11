from django.db import models
from accounts.models import Account
from datetime import date


class CashRecord(models.Model):
  account       = models.ForeignKey(Account, on_delete=models.RESTRICT)
  date          = models.DateField(default=date.today)
  balance       = models.DecimalField(max_digits=25, decimal_places=4)