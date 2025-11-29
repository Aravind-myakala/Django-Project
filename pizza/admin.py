from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'pizza_name', 'pizza_type', 'quantity', 'contact', 'ordered_at']

admin.site.register(Order, OrderAdmin)