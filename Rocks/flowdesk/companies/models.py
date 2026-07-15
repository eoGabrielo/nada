from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

