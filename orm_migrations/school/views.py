from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student


def students_list(request):
    students = Student.objects.order_by('group').prefetch_related('teacher')

    return render(request, 'school/students_list.html', {'object_list': students})
