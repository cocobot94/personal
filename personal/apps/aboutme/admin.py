from django.contrib import admin
from .models import AboutMe


# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("user", "id", "created")


admin.site.register(AboutMe, AboutMeAdmin)
