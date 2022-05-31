from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class usuario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    edad= forms.IntegerField()