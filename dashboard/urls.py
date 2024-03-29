from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', views.main, name='home'),    
    path('monthly_cash/', views.monthly_cash, name='monthly_cash'),    
    path('monthly_cash/<int:yr>/<int:mo>', views.monthly_cash, name='monthly_cash'),    
    path('utils/', views.get_utils, name='utils'),    
    path('testing/', views.testing, name='testing'),    
    # path('add/', views.add_account, name='add'),
    # path('detail/<int:ac_id>', views.details, name='details'),\  
]
