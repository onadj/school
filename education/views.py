# education/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Exercise

@login_required
def dashboard(request):
    subjects = Subject.objects.filter(teacher=request.user)
    return render(request, 'education/dashboard.html', {'subjects': subjects})

@login_required
def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'education/exercises.html', {'exercises': exercises})
