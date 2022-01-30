from django.contrib import admin
from .models import Member, Post, Service
from django.contrib.auth.models import Group, User

admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Service)
admin.site.unregister(Group)
admin.site.unregister(User)
