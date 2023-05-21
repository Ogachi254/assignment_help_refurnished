from django.contrib import admin
from .models import Contact, Order

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

