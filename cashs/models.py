from django.db import models
from accounts.models import Account
from datetime import date

# Create your models here.
from django.db import models

class CashRecord(models.Model):
  account       = models.ForeignKey(Account, on_delete=models.CASCADE)
  date          = models.DateField(default=date.today)
  balance       = models.DecimalField(max_digits=25, decimal_places=4)
  remark        = models.CharField(max_length=255, null=True, default=None, blank=True)
