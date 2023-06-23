from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    # path('record-all/', views.records, name='all'),
    path('test/', views.test, name='test'),   
]
