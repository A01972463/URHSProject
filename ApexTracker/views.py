from django.shortcuts import render

from .models import Student, Course

# Create your views here.
def index(request):
    return render(request, 'ApexTracker/index.html')

def input(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'ApexTracker/input.html',
                  {"students": students})

def report(request):
    return render(request, 'ApexTracker/report.html')

def settings(request):
    return render(request, 'ApexTracker/settings.html')

def new_student(request):
    return render(request, 'ApexTracker/set_new.html')

def edit_student(request):
    return render(request, 'ApexTracker/set_edit.html')

def quick_settings(request):
    return render(request, 'ApexTracker/set_quick_dis.html')
