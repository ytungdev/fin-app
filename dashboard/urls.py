from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', views.main, name='home'),    
    path('testing/', views.testing, name='testing'),    
    # path('add/', views.add_account, name='add'),
    # path('detail/<int:ac_id>', views.details, name='details'),\  
]
