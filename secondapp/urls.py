from django.urls import path
from . import  views

urlpatterns=[
   
    path('course_register/', views.course_register, name='course_register'),
]