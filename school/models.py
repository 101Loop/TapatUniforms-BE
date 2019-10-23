from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel

from TapatUniforms.static_var import GENDER_CHOICES


class School(CreateUpdateModel):
    name = models.CharField(verbose_name=_("School Name"), max_length=254)
    address = models.CharField(verbose_name=_("Full Address"), max_length=254)
    latitude = models.CharField(verbose_name=_("Latitude"), max_length=20)
    longitude = models.CharField(verbose_name=_("Longitude"), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")


class Student(CreateUpdateModel):
    student_id = models.CharField(verbose_name=_("Student ID"), max_length=100)
    name = models.CharField(verbose_name=_("Name"), max_length=254)
    standard = models.CharField(verbose_name=_("Class"), max_length=5)
    section = models.CharField(verbose_name=_("Section"), max_length=5)
    father_name = models.CharField(verbose_name=_("Father's Name"), max_length=255)
    gender = models.CharField(
        verbose_name=_("Gender"), choices=GENDER_CHOICES, max_length=1
    )
    email = models.CharField(verbose_name=_("Email"), max_length=254)
    mobile = models.CharField(verbose_name=_("Contact no."), max_length=20)
    school = models.ForeignKey(
        to=School, verbose_name=_("School"), on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("student_id", "school")
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
