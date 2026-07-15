from django.shortcuts import render
from django.http import HttpResponse

def home_company(request):
    return HttpResponse("Area de empresas")
