from django.urls import path

from .views import  HomePageView,  AboutPageView
from .views import contact_view

urlpatterns = [
    path('contact/', contact_view.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),
]