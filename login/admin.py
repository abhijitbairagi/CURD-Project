from atexit import register
from django.contrib import admin
from . models import userList
# Register your models here.
@admin.register(userList)
class UsarAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'password']
