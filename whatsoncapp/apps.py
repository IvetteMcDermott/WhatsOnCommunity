from django.apps import AppConfig


class WhatsoncappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'whatsoncapp'

    def ready(self):
        import whatsoncapp.signals