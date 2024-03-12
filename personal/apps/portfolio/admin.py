from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ["title", "id", "created", "order", "state"]


admin.site.register(Project, ProjectAdmin)
