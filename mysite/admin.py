# coding: utf-8
from django.contrib import admin
from django.utils.html import format_html
from mysite.models import *

class Profile_list(admin.ModelAdmin):
    fields = ('user', 'title','user_type','phone','email','status','start','finish')
    list_display = ('user', 'title','user_type','phone','email')
admin.site.register(Profile,Profile_list)

class StatusOfTasks_list(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)
admin.site.register(StatusOfTasks,StatusOfTasks_list)



class Tasks_lists(admin.ModelAdmin):
    fields = ('user','title', 'start','finish','description','comments','status')
    list_display = ('user','title', 'start','finish','description','comments','status')
admin.site.register(Tasks,Tasks_lists)

class Files_list(admin.ModelAdmin):
    fields = ('task','data')
    list_display = ('task','data')
admin.site.register(Files,Files_list)



