from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'stars', 'created_at']
    list_filter = ['stars']
    search_fields = ['user__username']

    # Customize the admin form if needed
    # form = ReviewAdminForm

    # Optionally, define any actions or additional admin methods
