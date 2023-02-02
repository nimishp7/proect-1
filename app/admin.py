from django.contrib import admin
from . models import *

# Register your models here.
class personModeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'password', 'contact']
