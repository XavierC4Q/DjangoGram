from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Follow, Like

class UserAdmin (admin.ModelAdmin):

    fieldsets = ((None, {'fields': ('username', 'email', 'city', 'country')}),)

    list_display = ('username', 'email', 'city', 'country', 'date_joined', 'last_login')


admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Like)
