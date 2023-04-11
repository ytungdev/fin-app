from django.contrib import admin
from .models import Stock, StockInOut

# Register your models here.

class StockAdmin(admin.ModelAdmin):
  list_display = ("name", "symbol", "market")

admin.site.register(Stock, StockAdmin)

class StockInOutAdmin(admin.ModelAdmin):
  list_display = ("stock_id", "price", "unit", "date")

admin.site.register(StockInOut, StockInOutAdmin)
