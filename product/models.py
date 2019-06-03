from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel


class Product(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Product"), max_length=254)
    sku = models.CharField(verbose_name=_("SKU Code"), max_length=254,
                           unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
