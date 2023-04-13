from django.urls import path
from . import views


app_name = 'stocks'
urlpatterns = [
    path('stocks/', views.StockList.as_view(), name='stocks'),    
    path('inouts/', views.inouts, name='inouts'),    
    path('view_stock/', views.view_stock, name='view_stock'),    
    path('view_stock/<int:stock_id>', views.view_stock, name='view_stock'),    
    path('add_inout/', views.add_inout, name='add_inout'),    
    path('add_inout/<int:stock_id>/', views.add_inout, name='add_inout'),    
]
