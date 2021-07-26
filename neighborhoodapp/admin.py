from .models import Business, Neighborhood, Profile, Post
from django.contrib import admin

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)