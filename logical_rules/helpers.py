import importlib
import sys
from django.conf import settings


def import_rules(app):

    try:
        app_path = importlib.import_module(app).__path__
    except AttributeError:
        return None

    try:
        module_spec = importlib.util.find_spec('rules', app_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
    except (ImportError, AttributeError):
        return None

    return module


def autodiscover():

    for app in settings.INSTALLED_APPS:
        import_rules(app)
