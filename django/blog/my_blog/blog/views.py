from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['post_date']

class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'
    oredering = ['post_date']

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

class UpdatePostview(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class CategoryView(CreateView):
    model = Category
    template_name = 'create_category.html'
    success_url = reverse_lazy('home')
    fields = '__all__'

def CategoryPageView(request, cats):
    category_details = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category_page.html', {'category':cats.title().replace('-',' '), 'category_details':category_details})