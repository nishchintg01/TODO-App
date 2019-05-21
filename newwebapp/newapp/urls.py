from django.urls import path
from .views import home,contact,Todoapp

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact),
    path('TodoApp',Todoapp,name='todoapp')
]
