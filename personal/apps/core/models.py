from django.db import models
from apps.users.models import User
from django.utils.translation import gettext as _


def custom_upload_to(instance, filename):
    if instance.pk:
        try:
            old_instance = Home.objects.get(pk=instance.pk)
            if old_instance and old_instance.image:
                old_instance.image.delete()
        except Home.DoesNotExist:
            pass
    return "home/" + filename


# Create your models here.
class Home(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    title = models.CharField(max_length=100, verbose_name=_("title"))
    content = models.TextField(max_length=1000, verbose_name=_("content"))
    image = models.ImageField(
        upload_to=custom_upload_to, blank=True, null=True, verbose_name=_("image")
    )

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Homes")
