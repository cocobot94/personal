from django.shortcuts import render
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import User


@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ("bio",)


# Create your views here.
