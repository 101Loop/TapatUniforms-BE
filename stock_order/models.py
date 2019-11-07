from django.db import models
from django.db.models import Sum
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel
from location.models import WareHouse
from product.models import Product
from outlet.models import Outlet


class IndentRequest(CreateUpdateModel):

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_("Quantity Required"))
    outlet = models.ForeignKey(
        verbose_name=_("Outlet"), to=Outlet, on_delete=models.CASCADE, null=True
    )
    requested_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Indent Requested On"), null=True
    )
    received_on = models.DateTimeField(
        verbose_name=_("Indent Received On"),
        blank=True,
        null=True,
        help_text="To update the admin, when the order is received",
    )

    def __str__(self):
        # return self.product.name
        return "{} - {}".format(self.product.name, self.outlet.short_name)

    class Meta:
        verbose_name = _("Indent Request")
        verbose_name_plural = _("Indent Request")


class Indent(CreateUpdateModel):

    indent_name = models.ForeignKey(
        to=IndentRequest,
        on_delete=models.CASCADE,
        verbose_name=_("Indent Name"),
        help_text="Name of the requested Indent",
        null=True,
    )
    price = models.DecimalField(
        verbose_name=_("Price"), decimal_places=2, max_digits=10
    )
    warehouse_name = models.ForeignKey(
        to=WareHouse,
        verbose_name=_("Shipping From"),
        on_delete=models.CASCADE,
        null=True,
    )
    # outlet = models.ForeignKey(
    #     verbose_name=_("Outlet"), to=Outlet, on_delete=models.CASCADE, null=True
    # )
    shipped_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Shipped On"), null=False, blank=False
    )

    @property
    def indent(self):
        return self.indent_name.product.name

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
        return self.indent_name.product.name

    class Meta:
        verbose_name = _("Indent")
        verbose_name_plural = _("Indents")


class Box(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Name"), max_length=10)
    box_code = models.CharField(verbose_name=_("Box code"), max_length=10)
    female_items = models.IntegerField(verbose_name=_("Number of female " "Items"))
    male_items = models.IntegerField(verbose_name=_("Number of Male Items"))
    indent = models.ForeignKey(to=Indent, on_delete=models.CASCADE)

    @property
    def total_item(self):
        return self.boxitem_set.all().aggregate(noi=Sum("num_of_item"))["noi"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")


class BoxItem(CreateUpdateModel):
    from outlet.models import OutletSubProduct

    product = models.ForeignKey(to=OutletSubProduct, on_delete=models.CASCADE)
    num_of_item = models.IntegerField(verbose_name=_("Quantity"))
    item_scanned = models.IntegerField(verbose_name=_("Item Scanned"), default=0)
    warehouse_stock = models.PositiveIntegerField(default=0)
    box = models.ForeignKey(to=Box, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = _("Box Item")
        verbose_name_plural = _("Box Items")
