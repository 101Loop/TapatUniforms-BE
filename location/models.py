from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel


class State(CreateUpdateModel):
    """ State Model : Will represent the States. """

    name = models.CharField(verbose_name=_("State Name"), max_length=30, unique=True)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.name


class City(CreateUpdateModel):
    """ City Model : Will represent all the cities which comes under respective States."""

    name = models.CharField(verbose_name=_("City"), max_length=50, unique=True)
    state = models.ForeignKey(
        to=State, on_delete=models.CASCADE, verbose_name=_("State")
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        unique_together = ("name", "state")

    def __str__(self):
        return "{} - {}".format(self.name, self.state)


class WareHouse(CreateUpdateModel):
    """ WareHouse Model : Will Represent the godown """

    name = models.CharField(verbose_name=_("WareHouse Name"), max_length=100)
    address = models.TextField(verbose_name=_("WareHouse Address"), null=True)
    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE,
        verbose_name=_("WareHouse City"),
        help_text="The city in which the WareHouse is.",
    )

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")
        unique_together = ("name", "city")

    def __str__(self):
        return "{} - {}".format(self.name, self.city)
