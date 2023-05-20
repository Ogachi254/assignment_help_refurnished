from django.urls import path, include
from .views import HomePageView, AboutPageView, contact_view, ContactView, success_page

urlpatterns = [
    path('success/', success_page, name='success_page'),
    path('contact/', ContactView.as_view(), name='save_contact'),
    path('contact/', contact_view.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
