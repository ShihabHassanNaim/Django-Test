from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'members/members.html')

def forms(request):
    return render(request, 'members/forms.html')