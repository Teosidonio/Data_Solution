from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'body','created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')

admin.site.register(Profile)
