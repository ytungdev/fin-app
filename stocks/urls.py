from django.urls import path
from . import views


app_name = 'stocks'
urlpatterns = [
    path('inouts/', views.inouts, name='inouts'),    
    path('add_inout/', views.add_inout, name='add_inout'),    
    path('add_inout/<int:stock_id>/', views.add_inout, name='add_inout'),    
]
