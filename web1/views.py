from django.shortcuts import render
from . import models

def list_students(request):
    all_students = models.student.objects.all()
    context = {'students': all_students}
    return render(request, 'web1/list.html', context=context)
