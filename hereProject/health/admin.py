from django.contrib import admin
from .models import Health, Category, Arm_Health, Exer_list, Gym_list, gymPlace, gymReview

# Register your models here.

admin.site.register(Health)
admin.site.register(Category)
admin.site.register(Arm_Health)
admin.site.register(Exer_list)
admin.site.register(Gym_list)
admin.site.register(gymPlace)
admin.site.register(gymReview)