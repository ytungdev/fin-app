from django.urls import path
from . import views


app_name = 'cashs'
urlpatterns = [
    path('record-add/', views.add_record, name='add'),
    path('load/', views.load, name="load"),
    path('record-all/', views.records, name='all'),
]
