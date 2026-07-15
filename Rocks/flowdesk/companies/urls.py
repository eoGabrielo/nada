from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.createCompany, name="company_create"),
]
