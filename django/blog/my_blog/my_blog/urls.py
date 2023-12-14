"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailsView.as_view(), name='article_detail'),
    path('post/create', views.CreatePostView.as_view(), name='create-post'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('post/update/<int:pk>', views.UpdatePostview.as_view(), name='update_post'),
    path('post/delete/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('category/<str:cats>', views.CategoryPageView, name='category_page')
]
