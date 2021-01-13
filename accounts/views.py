from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import AbstractUser
from django.db import models

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)