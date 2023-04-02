from django.urls import path
from . import views

urlpatterns = [
    path('record-all/', views.records, name='record-all'),
    path('record-add/', views.add_record, name='add_record'),    
]
