from django.contrib import admin
from .models import User
from django.utils.translation import gettext as _


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("username", "id", "email", "created", "is_active", "is_staff")


admin.site.register(User, UserAdmin)
