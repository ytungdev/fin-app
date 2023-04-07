from django.contrib import admin
from .models import CurrencyRecord

# Register your models here.

class CurrencyRecordAdmin(admin.ModelAdmin):
  list_display = ("date", "curr", "rate")

admin.site.register(CurrencyRecord, CurrencyRecordAdmin)