from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'post'

urlpatterns = [
    path('success/', views.post_success, name='post_success'),
    path('', login_required(views.post_list), name='post_list'),
    path('create/', login_required(views.post_create), name='post_create'),
]
