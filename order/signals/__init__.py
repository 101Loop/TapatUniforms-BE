import django.dispatch

post_save = django.dispatch.Signal(providing_args=["instance"])
