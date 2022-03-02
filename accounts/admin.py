from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
# Register your models here.
class userRegisterAdmin(admin.ModelAdmin):
    list_display = ('user')
    
admin.site.register(User)