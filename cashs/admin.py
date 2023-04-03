from django.contrib import admin
from .models import CashRecord

# Register your models here.

class CashRecordAdmin(admin.ModelAdmin):
  list_display = ("date", "account", "balance")

admin.site.register(CashRecord, CashRecordAdmin)