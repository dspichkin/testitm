from django.contrib import admin
from profile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'created', 'updated')
    list_filter = ['created']
    search_fields = ['username']
    date_hierarchy = 'created'

admin.site.register(Profile, ProfileAdmin)
