from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _


# Create your models here.
class Skill(models.Model):
    skill = models.CharField(max_length=70, unique=True, verbose_name=_("skill"))
    knowledge = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_("knowledge"),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"))

    def __str__(self) -> str:
        return self.skill

    class Meta:
        ordering = ["-knowledge"]
        verbose_name = _("skill")
        verbose_name_plural = _("skills")
