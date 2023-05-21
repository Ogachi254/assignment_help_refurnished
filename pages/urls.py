from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactView,
    OrderView,
    success_page,
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='save_contact'),
    path('order/', login_required(OrderView.as_view()), name='save_order'),
    path('success/', success_page, name='success_page'),
]
