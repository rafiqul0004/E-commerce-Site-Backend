from django.contrib import admin
from django.contrib.auth.models import User
from .models import User
# Register your models here.   
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_no']

    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(User, UserAdmin)