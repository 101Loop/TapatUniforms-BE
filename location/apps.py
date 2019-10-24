from django.apps import AppConfig


class LocationConfig(AppConfig):
    name = "location"
    verbose_name = "Location"

    def ready(self):
        pass
