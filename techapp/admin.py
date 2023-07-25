from django.contrib import admin
from .models import *

class AdminState(admin.ModelAdmin):
    list_display=['name','created_on','updated_on']

class AdminCity(admin.ModelAdmin):
    list_display=['name','created_on','updated_on']

class AdminBranch(admin.ModelAdmin):
    list_display=['name','created_on','updated_on']

admin.site.register(State,AdminState)
admin.site.register(City,AdminCity)
admin.site.register(Branch,AdminBranch)

