from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'post'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    context_object_name = 'post'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'pages/post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'pages/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')
