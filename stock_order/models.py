from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel


class IndentRequest(CreateUpdateModel):
    from product.models import Product
    from school.models import School

    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name=_("Quantity Required"))
    school = models.ForeignKey(verbose_name=_("School"), to=School,
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _("Indent Request")
        verbose_name_plural = _("Indent Request")


class Indent(CreateUpdateModel):
    from school.models import School

    name = models.CharField(verbose_name=_("Indent Name"), max_length=100)
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2,
                                max_digits=10)
    shipping_from = models.CharField(verbose_name=_("Shipping From"),
                                     max_length=254)
    shipping_from_lat = models.CharField(verbose_name=_("Shipping from "
                                                        "Latitude"),
                                         max_length=20)
    shipping_from_long = models.CharField(verbose_name=_("Shipping from "
                                                         "Longitude"),
                                          max_length=20)
    school = models.ForeignKey(verbose_name=_("School"), to=School,
                               on_delete=models.PROTECT)
    shipped_on = models.DateTimeField(verbose_name=_("Shipped On"),
                                      null=False, blank=False)
    received_on = models.DateTimeField(verbose_name=_("Received On"),
                                       blank=True, null=True)

    @property
    def num_of_boxes(self):
        return self.box_set.count()

    @property
    def num_of_items(self):
        item_count = 0
        
        for box in self.box_set.all():
            item_count += box.total_item
        
        return item_count

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Indent")
        verbose_name_plural = _("Indents")


class Box(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Name"), max_length=10)
    box_code = models.CharField(verbose_name=_("Box code"), max_length=10)
    female_items = models.IntegerField(verbose_name=_("Number of female "
                                                      "Items"))
    male_items = models.IntegerField(verbose_name=_("Number of Male Items"))
    indent = models.ForeignKey(to=Indent, on_delete=models.PROTECT)

    @property
    def total_item(self):
        item_count = 0

        for item in self.boxitem_set.all():
            item_count += item.num_of_item

        return item_count

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")


class BoxItem(CreateUpdateModel):
    from outlet.models import OutletSubProduct

    product = models.ForeignKey(to=OutletSubProduct, on_delete=models.PROTECT)
    num_of_item = models.IntegerField(verbose_name=_("Quantity"))
    item_scanned = models.IntegerField(verbose_name=_("Item Scanned"),
                                       default=0)
    box = models.ForeignKey(to=Box, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = _("Box Item")
        verbose_name_plural = _("Box Items")
