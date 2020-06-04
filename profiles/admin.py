from django.contrib import admin

from .models import Profile, Education, Experience


class ProfileAdmin(admin.ModelAdmin):
  list_display = [
    'user','linkedin' , 'profession', 'country', 'created_at'
  ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education)
admin.site.register(Experience)