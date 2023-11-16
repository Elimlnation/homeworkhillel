from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from faker import Faker

def generate_student(request):
    faker = Faker()
    student = Student.objects.create(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=faker.random_int(min=18, max=25)
    )
    data = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
    }
    return JsonResponse(data)

def generate_students(request):
    count = int(request.GET.get('count', 1))
    if 0 < count <= 100:
        students = []
        for _ in range(count):
            faker = Faker()
            student = Student.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=faker.random_int(min=18, max=25)
            )
            students.append({
                'id': student.id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'age': student.age,
            })
        return JsonResponse(students, safe=False)
    else:
        return JsonResponse({'error': 'Invalid count value'})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})
