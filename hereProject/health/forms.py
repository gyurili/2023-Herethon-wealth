from django import forms
from .models import gymReview

class PostModelForm(forms.ModelForm):
    class Meta:
        model = gymReview
        # 어떤 필드를 입력 받을지 써주기
        fields = ['title', 'body']