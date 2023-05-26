from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'post'

urlpatterns = [
    path('', login_required(views.post_list), name='post_list'),
    path('create/', login_required(views.post_create), name='post_create'),
    path('edit/<int:pk>/', login_required(views.post_edit), name='post_edit'),
    path('delete/<int:pk>/', login_required(views.post_delete), name='post_delete'),
    path('success/', views.post_success, name='post_success'),
]
