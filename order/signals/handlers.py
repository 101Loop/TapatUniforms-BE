from django.dispatch import receiver
from django.db.models.signals import post_save
from order.models import SubOrder, Order
from drfaddons.utils import send_message


@receiver(post_save, sender=Order)
def post_order(sender, instance: Order, created, **kwargs):
    INVOICE_URL = "https://tapatapi.civilmachines.com/api/order/invoice/"
    # INVOICE_URL = "http://192.168.1.247:8000/api/order/invoice/"
    invoice_url = INVOICE_URL + "{}/".format(instance.id)
    message = (
        "Thank You for ordering from us. Your invoice can be downloaded from "
        + invoice_url
    )
    subject = "Invoice"
    data = {
        "message": message,
        "subject": subject,
        "recip": [instance.mobile],
        "recip_email": [instance.email],
    }

    if created:
        send_message(**data)
