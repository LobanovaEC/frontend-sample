from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'slug')
    list_display_links = ('user', 'slug')



