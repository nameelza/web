from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def list_results(request):
    return render(request, 'student/results.html')

def rental(request):
    return render(request, 'student/rental.html')

def profile(request):
    return render(request, 'student/profile.html')

def create(request):
    return render(request, 'student/create.html')