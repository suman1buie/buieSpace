from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *


class UserAdmin(ModelAdmin):
	list_display  = ['user']
	search_fields = ['user']
	list_filter   = ['user']

admin.site.register(Catagory)
admin.site.register(UserProfile,UserAdmin)
admin.site.register(Atrical)
admin.site.register(Academic)
admin.site.register(Trade)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Study)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Metarial)
admin.site.register(Sellybus)
