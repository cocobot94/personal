from django.db import models
from django.utils.translation import gettext as _
from apps.users.models import User


# Create your models here.


class CategoryProject(models.Model):
    description = models.CharField(
        max_length=60, verbose_name="category product", unique=True
    )


class Project(models.Model):
    user = models.ManyToManyField(User, verbose_name=_("user"))
    title = models.CharField(verbose_name=_("title"), max_length=100)
    description = models.TextField(verbose_name=_("description"))
    link = models.URLField()
    image = models.ImageField(
        upload_to="projects/", blank=True, null=True, verbose_name=_("image")
    )
    order = models.PositiveSmallIntegerField(verbose_name=_("order"))
    state = models.BooleanField(default=True, verbose_name=_("state"))
    categoryproject = models.ManyToManyField(
        CategoryProject, verbose_name=_("categoty project"), blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ["order"]
