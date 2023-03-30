from django.db import models

class Account(models.Model):
  location  = models.CharField(max_length=255)
  name      = models.CharField(max_length=255)
  provider  = models.CharField(max_length=255)
  remark    = models.CharField(max_length=255)