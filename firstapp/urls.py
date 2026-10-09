
from django.urls import path
from . import  views

urlpatterns=[
    #path('profile/',views.profile,name='profile'),
    #path('gallery/',views.gallery,name='gallery'),
    #path('marks_calculator/',views.marks_calculator,name='marks_calculator'),
    #path('quiz/',views.quiz,name='quiz'),
    #path('clgDept/',views.clgDept,name='clgDept'),
    # path('studentForm/', views.studentForm, name='studentForm'),
    # path('employee_register/', views.employee_register, name='employee_register'),
    path('course_register/', views.course_register, name='course_register'),
]