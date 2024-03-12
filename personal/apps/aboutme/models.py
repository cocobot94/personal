from django.db import models
from apps.users.models import User
from django.utils.translation import gettext as _


def custom_upload_to_cv(instance, filename):
    try:
        old_instance = AboutMe.objects.filter(pk=instance.pk).first()
        if old_instance and old_instance.cv:
            old_instance.cv.delete()
        return "aboutme/" + filename
    except AboutMe.DoesNotExist:
        return "aboutme/" + filename


def custom_upload_to_image(instance, filename):
    try:
        old_instance = AboutMe.objects.filter(pk=instance.pk).first()
        if old_instance and old_instance.image:
            old_instance.image.delete()
        return "aboutme/" + filename
    except AboutMe.DoesNotExist:
        return "aboutme/" + filename


# Create your models here.
class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("description"))
    cv = models.FileField(upload_to=custom_upload_to_cv, null=True, blank=True)
    image = models.ImageField(
        upload_to=custom_upload_to_image, null=True, blank=True, verbose_name=_("image")
    )
    videoUrl = models.URLField(default="#", null=True, blank=True)
    state = models.BooleanField(default=True, verbose_name=_("state"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"))

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _("About Me")
        verbose_name_plural = _("About Me")
