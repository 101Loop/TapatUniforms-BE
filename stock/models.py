from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel


class Stock(CreateUpdateModel):
    from outlet.models import OutletProduct

    outlet_product = models.ForeignKey(to=OutletProduct,
                                       verbose_name=_("Outlet Product"),
                                       on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    location = models.CharField(verbose_name=_("Storage Location"),
                                max_length=10)

    def __str__(self):
        return str(self.outlet_product)

    class Meta:
        unique_together = ('outlet_product', 'location')
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')
