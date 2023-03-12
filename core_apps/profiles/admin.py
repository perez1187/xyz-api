from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user"]
    list_filter = ["user"]
    list_display_links = ["id", "pkid"]

admin.site.register(Profile, ProfileAdmin)