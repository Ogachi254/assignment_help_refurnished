from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ReviewListView, ReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('', login_required(ReviewListView.as_view()), name='review_list'),
    path('create/', login_required(ReviewCreateView.as_view()), name='review_create'),
]
