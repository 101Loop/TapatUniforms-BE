from django.db import models
from django.utils.text import gettext_lazy as _
from drf_user.models import User

from outlet.models import Outlet


class Manager(models.Model):
    outlet = models.ForeignKey(
        verbose_name=_("Outlet"), to=Outlet, on_delete=models.PROTECT
    )
    user = models.OneToOneField(
        verbose_name=_("User"), to=User, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.user.name

    class Meta:
        unique_together = ("outlet", "user")
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
