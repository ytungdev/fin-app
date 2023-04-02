from django.db import models

class Account(models.Model):
  location  = models.CharField(max_length=255)
  name      = models.CharField(max_length=255)
  provider  = models.CharField(max_length=255)
  curr      = models.CharField(max_length=255, default="HKD")
  remark    = models.CharField(max_length=255, null=True, default=None, blank=True)

  def __str__(self):
    return f"[{self.location}]{self.name}"