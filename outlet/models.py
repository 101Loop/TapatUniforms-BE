from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel

from TapatUniforms.static_var import PRODUCT_CHOICES


class Outlet(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Name"), max_length=254)
    location = models.CharField(verbose_name=_("Location"), max_length=254)
    short_name = models.CharField(verbose_name=_("Short Name"), max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Outlet')
        verbose_name_plural = _('Outlets')


class OutletProduct(CreateUpdateModel):
    from product.models import Product

    outlet = models.ForeignKey(to=Outlet, verbose_name=_("Outlet"),
                               on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, verbose_name=_("Product"),
                                on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10,
                                decimal_places=3)
    image = models.ImageField(verbose_name=_("Image"))
    color = models.CharField(verbose_name=_("Color"), max_length=254,
                             default=_("white"))
    color_code = models.CharField(verbose_name=_("Color Code"),
                                  max_length=254, default=_("#fff"))
    size = models.CharField(verbose_name=_("Size"), max_length=4,
                            choices=PRODUCT_CHOICES, default='24')
    warehouse_stock = models.IntegerField(verbose_name=_("Warehouse Stock"),
                                          default=0)
    display_stock = models.IntegerField(verbose_name=_("Display Stock"),
                                        default=0)

    def __str__(self):
        return "{}, {}".format(str(self.product), str(self.outlet))

    class Meta:
        unique_together = ('outlet', 'product')
        verbose_name = _("Outlet Product")
        verbose_name_plural = _("Outlet Products")

