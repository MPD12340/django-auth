from django.contrib import admin
from app.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'is_admin', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
