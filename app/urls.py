# app/urls.py

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('blog/create/', CreateBlogView.as_view(), name='blog_create'),
    path('category/create/', BlogCategoryCreateView.as_view(), name='category_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
