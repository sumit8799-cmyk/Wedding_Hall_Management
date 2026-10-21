from django.apps import AppConfig


class CommanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comman'

    def ready(self):
        """
        Load signals when app is ready
        """
        import comman.signals
        
from django.apps import AppConfig

class CommanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comman'