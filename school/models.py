from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel


class School(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Name"), max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')


class Student(CreateUpdateModel):
    id_no = models.CharField(verbose_name=_("ID Number"), max_length=100)
    name = models.CharField(verbose_name=_("Name"), max_length=254)
    school = models.ForeignKey(to=School, verbose_name=_("School"),
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('id_no', 'school')
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
