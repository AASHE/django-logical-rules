import imp
from importlib import import_module
from django.conf import settings


def import_rules(app):

    try:
        app_path = import_module(app).__path__
    except AttributeError:
        return None

    try:
        imp.find_module('rules', app_path)
    except ImportError:
        return None

    module = import_module('%s.rules' % app)
    return module


def autodiscover():

    for app in settings.INSTALLED_APPS:
        import_rules(app)
