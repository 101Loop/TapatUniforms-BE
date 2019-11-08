from django.dispatch import receiver
from django.db.models.signals import post_save
from order.models import SubOrder
from django.http import HttpResponse
from drfaddons.utils import send_message


@receiver(post_save, sender=SubOrder)
def post_order(instance, created, **kwargs):
    pass
