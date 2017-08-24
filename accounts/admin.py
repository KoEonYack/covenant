from django.contrib import admin
from .models import Profile
# Register your models here.


#class UserAdmin(admin.ModelAdmin):
#    list_display = "__all__"
#    list_display = ['user', 'realname', 'student_number', 'class_name', ]

admin.site.register(Profile)