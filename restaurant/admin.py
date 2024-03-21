from django.contrib import admin

# Register your models here.
# In admin.py

from .models import Menu, Booking

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'inventory']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'guests', 'booking_date']
