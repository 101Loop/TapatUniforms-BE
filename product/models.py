from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel

from TapatUniforms.static_var import PRODUCT_CHOICES


class CategoryMaster(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Category"), max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Product"), max_length=254)
    sku = models.CharField(verbose_name=_("SKU Code"), max_length=254,
                           unique=True)
    size = models.CharField(verbose_name=_("Size"), max_length=254,
                            choices=PRODUCT_CHOICES)
    category = models.ForeignKey(to=CategoryMaster, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
