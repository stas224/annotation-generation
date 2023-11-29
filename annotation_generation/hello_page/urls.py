from django.urls import path
from . import views

app_name = 'hello_page'

urlpatterns = [
    path('', views.method, name='method'),
]
