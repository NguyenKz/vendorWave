from django.apps import AppConfig


class MerchantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.merchants'
    
    def ready(self) -> None:
        import apps.merchants.signals
        return super().ready()
