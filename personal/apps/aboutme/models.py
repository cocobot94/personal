from django.db import models
from apps.users.models import User
from django.utils.translation import gettext as _


def custom_upload_to_cv(instance, filename):
    try:
        old_instance = AboutMe.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.cv.delete()
        return "aboutme/" + filename
    except AboutMe.DoesNotExist:
        return "aboutme/" + filename


def custom_upload_to_video(instance, filename):
    try:
        old_instance = AboutMe.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.video.delete()
        return "aboutme/" + filename
    except AboutMe.DoesNotExist:
        return "aboutme/" + filename


# Create your models here.
class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("description"))
    cv = models.FileField(upload_to=custom_upload_to_cv, null=True, blank=True)
    video = models.FileField(upload_to=custom_upload_to_video, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _("About Me")
        verbose_name_plural = _("About Me")
