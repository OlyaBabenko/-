from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'profile_picture', 'gender')
