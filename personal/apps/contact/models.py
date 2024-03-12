from django.db import models
from django.utils.translation import gettext as _
from apps.users.models import User


# Create your models here.
class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("description"))
    phone = models.IntegerField(verbose_name=_("phone"))
    address = models.CharField(max_length=150, verbose_name=_("address"))
    email = models.EmailField(verbose_name=_("email"))
    website = models.URLField(verbose_name=_("website"))

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _("Info")
        verbose_name = _("Infos")
