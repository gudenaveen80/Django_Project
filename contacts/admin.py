from django.contrib import admin
from .models import Contact, ContactMessage

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject', 'number', 'created_at')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'email', 'subject')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
