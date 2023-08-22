from django.contrib import admin

# Register your models here.
from Userauth.models import Users


class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_active','otp','access_token')
    # exclude = ['password']
admin.site.register(Users, UserAuthAdmin)