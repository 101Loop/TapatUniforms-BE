from django.dispatch import receiver
from django.db.models.signals import post_save
from order.models import SubOrder
from drfaddons.utils import send_message


@receiver(post_save, sender=SubOrder)
def post_order(sender, instance: SubOrder, created, **kwargs):
    invoice_url = (
        "https://tapatapi.civilmachines.com/api/order/invoice/"
        + "{}/".format(instance.id)
    )
    message = (
        "Thank You for ordering from us. Your invoice can be downloaded from "
        + invoice_url
    )
    subject = "Invoice"
    data = {
        "message": message,
        "subject": subject,
        "recip": [instance.order.email],
        "recip_email": [instance.order.email],
    }

    if created:
        send_message(**data)
