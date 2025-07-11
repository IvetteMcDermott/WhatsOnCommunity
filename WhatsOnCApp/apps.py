from django.apps import AppConfig


class WhatsoncappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WhatsOnCApp'

    def ready(self):
        import WhatsOnCApp.signals