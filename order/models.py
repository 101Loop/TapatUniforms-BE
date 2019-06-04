from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel


class Order(CreateUpdateModel):
    from outlet.models import Outlet

    name = models.CharField(verbose_name=_("Buyer Name"), max_length=254)
    mobile = models.CharField(verbose_name=_("Buyer Mobile Number"),
                              max_length=15)
    email = models.CharField(verbose_name=_("Buyer Email"), max_length=500)

    total = models.DecimalField(verbose_name=_("Total Amount"),
                                decimal_places=2, max_digits=10)
    discount = models.DecimalField(verbose_name=_("Discount Amount"),
                                   decimal_places=2, max_digits=10)

    outlet = models.ForeignKey(to=Outlet, verbose_name=_("Outlet"),
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class SubOrder(CreateUpdateModel):
    from outlet.models import OutletProduct

    order = models.ForeignKey(to=Order, on_delete=models.PROTECT,
                              verbose_name=_("Order"))
    product = models.ForeignKey(to=OutletProduct, on_delete=models.PROTECT,
                                verbose_name=_("Outlet Product"))
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2,
                                max_digits=10)
