from django.dispatch import receiver
from django.db.models.signals import post_save
from order.models import SubOrder
import environ
from drfaddons.utils import send_message

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()


@receiver(post_save, sender=SubOrder)
def post_order(sender, instance: SubOrder, created, **kwargs):
    invoice_url = env("INVOICE_URL") + "{}/".format(instance.id)
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
