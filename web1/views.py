from django.shortcuts import render
from . import models
from .models import Learner

def list_students(request):
    all_students = models.Learner.objects.all()
    context = {"students": all_students}
    return render(request, "web1/list.html",context=context)



