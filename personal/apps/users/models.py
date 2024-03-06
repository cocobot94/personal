from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


def custom_upload_to(instance, filename):
    try:
        old_instance = User.objects.filter(pk=instance.pk).first()
        if old_instance.image:
            old_instance.image.delete()
        return "users/" + filename
    except User.DoesNotExist:
        return "users/" + filename


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(
        upload_to=custom_upload_to, null=True, blank=True, verbose_name=_("Image")
    )
    bio = models.TextField(verbose_name=_("Bio"), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["-created"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")
