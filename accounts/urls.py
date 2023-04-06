from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.AccountList.as_view(), name='all'),    
    path('add/', views.add_account, name='add'),
    path('detail/<int:ac_id>', views.details, name='details'),
]
