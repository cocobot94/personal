from django.contrib import admin
from .models import Skill


# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ["skill", "knowledge"]


admin.site.register(Skill, SkillAdmin)
