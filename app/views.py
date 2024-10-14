from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

class HomeView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'home.html', {'blogs': blogs})

class CustomLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # เปลี่ยนเส้นทางหลังจากล็อกอินสำเร็จ
        return render(request, 'login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # เปลี่ยนเส้นทางหลังจากลงทะเบียนสำเร็จ
        return render(request, 'register.html', {'form': form})  # ส่งคืนฟอร์มพร้อมข้อผิดพลาดถ้ามี
    
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # เปลี่ยนเส้นทางหลังจากล็อกเอาท์

class CreateBlogView(LoginRequiredMixin, View):
    def get(self, request):
        form = BlogForm()
        return render(request, 'blog_create.html', {'form': form})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # บันทึกผู้ใช้ที่ล็อกอินเป็นผู้เขียน
            blog.save()
            return redirect('blog_detail', blog.id)  # เปลี่ยนเส้นทางไปยังบล็อกที่สร้างใหม่
        return render(request, 'blog_create.html', {'form': form})
    

class BlogCategoryCreateView(View):
    def get(self, request):
        form = BlogCategoryForm()
        return render(request, 'blog_category_create.html', {'form': form})
    
    def post(self, request):
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'blog_category_create.html', {'form': form})

class BlogDetailView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, 'blog_detail.html', {'blog': blog, 'year': datetime.now().year})
