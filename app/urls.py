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
    path('activity/', ActivityView.as_view(), name='activity'),
    path('activity/hobby/', HobbyView.as_view(), name='hobby'),
    path('activity/hobby/detail/', HobbyDetailView.as_view(), name='hobby_detail'),
    path('activity/mood/', MoodView.as_view(), name='mood'),
    path('activity/mood/detail/', MoodDetailView.as_view(), name='mood_detail'),
    path('activity/health/', HealthView.as_view(), name='health'),
    path('activity/health/detail/', HealthDetailView.as_view(), name='health_detail'),
    path('activity/technology/detail/', TechnologyDetailView.as_view(), name='tech_detail'),
    path('activity/technology/', TechnologyView.as_view(), name='tech'),
    path('work/',WorkView.as_view(), name='work'),
    path('detail-work/', WorkDetailView.as_view(),name='detailwork'),
    path('news/', NewsView.as_view(), name='news'),
    path('news-page1/', NewsPageOneView.as_view(), name='news-page1'),
    path('news-page2/', NewsPageTwoView.as_view(), name='news-page2'),
    path('news-page3/', NewsPageThreeView.as_view(), name='news-page3'),
    path('news-page4/', NewsPageFourView.as_view(), name='news-page4'),
   
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
