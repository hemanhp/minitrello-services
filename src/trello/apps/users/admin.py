from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, OTPRequest
# Register your models here.

admin.site.register(OTPRequest)

@admin.register(User)
class AppUserAdmin(UserAdmin):
    pass