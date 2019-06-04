from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel


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
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10,
                                decimal_places=3)
    category = models.ForeignKey(to=CategoryMaster, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(CreateUpdateModel):
    image = models.ImageField(verbose_name=_("Image"))
    product = models.ForeignKey(to=Product, verbose_name=_("Product"),
                                on_delete=models.PROTECT)

    def __str__(self):
        return 'image: {}, product: {}'.format(self.image, self.product)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
