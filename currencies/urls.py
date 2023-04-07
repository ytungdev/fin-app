from django.urls import path
from . import views


app_name = 'currencies'
urlpatterns = [
    # path('record-all/', views.records, name='all'),
    path('record-add/', views.add_record, name='add'),    
]
