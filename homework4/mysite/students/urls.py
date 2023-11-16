from django.urls import path
from .views import generate_student, generate_students, students_list

urlpatterns = [
    path('generate-student/', generate_student, name='generate_student'),
    path('generate-students/', generate_students, name='generate_students'),
    path('', students_list, name='students_list'),
]