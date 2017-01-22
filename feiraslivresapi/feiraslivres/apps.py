from django.apps import AppConfig


class FeiraslivresConfig(AppConfig):
    name = 'feiraslivres'

    def ready(self):
        import feiraslivres.signals
