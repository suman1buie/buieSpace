from django.apps import AppConfig


class CollageappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'collageapp'
    def ready(self):
        import collageapp.mysignal