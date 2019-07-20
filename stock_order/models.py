from django.db import models
from drfaddons.models import CreateUpdateModel
from django.utils.text import gettext_lazy as _


class IndentRequest(CreateUpdateModel):
    from school.models import School
    school = models.ForeignKey(to=School, on_delete=models.PROTECT)

    def __str__(self):
        return self.school.name

    class Meta:
        verbose_name = _("Indent Request")
        verbose_name_plural = _("Indent Requests")


class IndentRequestDetail(CreateUpdateModel):
    from product.models import Product
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name=_("Quantity Required"))
    indent_request = models.ForeignKey(to=IndentRequest,
                                       on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _("Indent Request Detail")
        verbose_name_plural = _("Indent Request Details")


class Indent(CreateUpdateModel):
    from school.models import School
    name = models.CharField(verbose_name=_("Indent Name"), max_length=100)
    num_of_boxes = models.IntegerField(verbose_name=_("Number of Boxes"))
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2,
                                max_digits=10)
    shipping_from = models.CharField(verbose_name=_("Shipping From"),
                                     max_length=254)
    shipping_to = models.ForeignKey(to=School, on_delete=models.PROTECT)
    shipping_from_lat = models.CharField(verbose_name=_("Shipping from "
                                                        "Latitude"),
                                         max_length=20)
    shipping_from_long = models.CharField(verbose_name=_("Shipping from "
                                                         "Longitude"),
                                          max_length=20)
    indent_request = models.ForeignKey(to=IndentRequest,
                                       on_delete=models.PROTECT)

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
    total_item = models.IntegerField(verbose_name=_("Total Items"))
    indent = models.ForeignKey(to=Indent, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")


class BoxItem(CreateUpdateModel):
    from outlet.models import OutletProduct
    product = models.ForeignKey(to=OutletProduct, on_delete=models.PROTECT)
    num_of_item = models.IntegerField(verbose_name=_("Number of Items"))
    item_scanned = models.IntegerField(verbose_name=_("Item Scanned"))
    item_in_shelf = models.IntegerField(verbose_name=_("Items in shelf"))
    box = models.ForeignKey(to=Box, on_delete=models.PROTECT)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = _("Box Item")
        verbose_name_plural = _("Box Items")
