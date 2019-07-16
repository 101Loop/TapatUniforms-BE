from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel

from TapatUniforms.static_var import GENDER_CHOICES, MALE, PRODUCT_TYPE_CHOICES


class CategoryMaster(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Category"), max_length=254)
    image = models.ImageField(verbose_name=_("Image"), null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Product"), max_length=254)
    sku = models.CharField(verbose_name=_("SKU Code"), max_length=254,
                           unique=True)
    category = models.ForeignKey(to=CategoryMaster, on_delete=models.PROTECT)
    gender_type = models.CharField(verbose_name=_("Gender"),
                                   max_length=254, choices=GENDER_CHOICES,
                                   default=MALE)
    product_type = models.CharField(verbose_name=_("Product Type"),
                                    choices=PRODUCT_TYPE_CHOICES,
                                    max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
