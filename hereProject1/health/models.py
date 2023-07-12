from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class gymPlace(models.Model):
    placeName = models.CharField(verbose_name="이름", max_length=128)
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_gyms', blank=True)

    def __str__(self):
        return self.placeName
    
class gymReview(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")

    def __str__(self):
        return self.title