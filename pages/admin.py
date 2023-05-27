from django.contrib import admin
from .models import Contact, Order, WriterBid

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(WriterBid)
class WriterBidAdmin(admin.ModelAdmin):
    pass
