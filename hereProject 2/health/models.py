from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Health(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length=10)
    
    def __str__(self):
        return self.category
    
class Arm_Health(models.Model):
    arm_name = models.CharField(max_length=20)
    content = models.TextField(null=True)
    
    def __str__(self):
        return self.arm_name
    
class Exer_list(models.Model):
    arm_name = models.CharField(max_length=20)
    content = models.TextField(null=True)
    
    def __str__(self):
        return self.arm_name

class Gym_list(models.Model):
    gym_name = models.CharField(max_length=20)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.gym_name
    
# Create your models here.
class gymPlace(models.Model):
    placeName = models.CharField(verbose_name="이름", max_length=128)
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='blog_photo')
    likes = models.ManyToManyField(User, related_name='liked_gyms', blank=True)

    def __str__(self):
        return self.placeName
    
class gymReview(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")

    def __str__(self):
        return self.title
    
# Create your models here.