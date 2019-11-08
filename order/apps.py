from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = "order"

    def ready(self):
        from .signals.handlers import post_order

        pass
