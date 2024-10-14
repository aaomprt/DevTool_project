from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def blog_image_upload_path(instance, filename):
    # เปลี่ยนชื่อไฟล์ให้เป็น pk ของบล็อก
    return f'blog_images/{instance.pk}.jpg'

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)  # ไม่ต้องเปลี่ยน
    content = models.TextField(blank=False)  # ไม่ต้องเปลี่ยน
    image = models.ImageField(upload_to='blog_images/', blank=True)  # อนุญาตให้เป็นว่าง
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(BlogCategory, blank=True)  # อนุญาตให้เป็นว่าง
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # อนุญาตให้เป็นว่างและเป็น null

    def __str__(self):
        return self.title
