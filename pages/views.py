from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'post_list'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
# Create your views here.
