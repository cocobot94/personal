from typing import Any
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView

from .models import Home
from apps.users.models import User
from apps.portfolio.models import Project
from apps.skills.models import Skill
from apps.aboutme.models import AboutMe

from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions


# Create your views here.


class homeTemplateView(View):
    template_name = "core/home.html"

    def get(self, request):
        context = {}
        context["home"] = Home.objects.all().first()
        context["projects"] = Project.objects.filter(state=True)
        context["aboutme"] = AboutMe.objects.filter(state=True).first()
        context["skills"] = Skill.objects.all()
        return render(request, self.template_name, context)


@register(Home)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ("description",)
