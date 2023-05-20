from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'comment', 'user_image', 'comment_image']
