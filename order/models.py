from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel

from TapatUniforms.static_var import DISCOUNT_CHOICES


class Discount(CreateUpdateModel):
    product_quantity = models.IntegerField(verbose_name=_("Number of "
                                                          "Items"))
    discount_type = models.CharField(verbose_name=_("Discount "
                                                    "Type"),
                                     choices=DISCOUNT_CHOICES, max_length=3
                                     , default='A')
    value = models.IntegerField(verbose_name="Value", default=0
                                )

    def __str__(self):
        return "Discount on {}".format(str(self.product_quantity), )

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")


class Order(CreateUpdateModel):
    from outlet.models import Outlet

    name = models.CharField(verbose_name=_("Buyer Name"), max_length=254)
    mobile = models.CharField(verbose_name=_("Buyer Mobile Number"),
                              max_length=15)
    email = models.CharField(verbose_name=_("Buyer Email"), max_length=500)
    discount = models.IntegerField(verbose_name=_("Discount"))
    outlet = models.ForeignKey(to=Outlet, verbose_name=_("Outlet"),
                               on_delete=models.PROTECT)

    @property
    def payment_done(self):
        total = 0
        for x in self.transaction_set.all():
            total += x.amount
        return total >= self.total

    @property
    def total(self):
        total = 0
        for x in self.suborder_set.all():
            total += x.total
        return total

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class SubOrder(CreateUpdateModel):
    from outlet.models import OutletSubProduct

    order = models.ForeignKey(to=Order, on_delete=models.PROTECT,
                              verbose_name=_("Order"))
    product = models.ForeignKey(to=OutletSubProduct, on_delete=models.PROTECT,
                                verbose_name=_("Outlet Product"))
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2,
                                max_digits=10)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

    @property
    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.order.name

    class Meta:
        verbose_name = _("SubOrder")
        verbose_name_plural = _("Sub Orders")


class Transaction(CreateUpdateModel):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT,
                              verbose_name=_("Order"))
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=10,
                                 decimal_places=2)
    mode = models.CharField(verbose_name=_("Mode of Payment"), max_length=254)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
