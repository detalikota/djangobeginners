from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/post_new.html'
    fields = ('title', 'body')
    login_url = 'login' 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'pages/post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
     

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login' 
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
