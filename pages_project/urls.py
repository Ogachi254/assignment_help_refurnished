from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps
    path('post/', include('posts.urls')),
    path('reviews/', include('reviews.urls')),
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
