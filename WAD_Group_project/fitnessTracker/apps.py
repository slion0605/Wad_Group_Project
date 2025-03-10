from django.apps import AppConfig


class FitnessTrackerConfig(AppConfig):
    name = 'fitnessTracker'

    def ready(self):
        import fitnessTracker.signals 
