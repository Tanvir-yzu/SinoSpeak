# accounts/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_profile_image')  # Fields to display in the list view
    search_fields = ('user__username',)  # Enable search by username
    list_filter = ('user',)  # Add a filter for users

    def display_profile_image(self, obj):
        """Custom method to display the profile image in the admin list view."""
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.profile_image.url)
        return "No Image"
    
    display_profile_image.short_description = 'Profile Image'  # Column header in admin

# Register the Profile model with the custom admin class
admin.site.register(Profile, ProfileAdmin)