from django.apps import AppConfig
import logging

class TeamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teams'

    verbose_name = "Эфективная команда "
    verbose_name_plural = ""

    def ready(self):
        logging.warning(f'Model {self.name} is ready ')