import os
import sys
import django

BASE_PATH = os.path.dirname(__file__)

def main():
    """
    Standalone django model test with a 'memory-only-django-installation'.
    You can play with a django model without a complete django app installation.
    http://www.djangosnippets.org/snippets/1044/
    """
    sys.exc_clear()

    os.environ["DJANGO_SETTINGS_MODULE"] = "django.conf.global_settings"

    from django.conf import global_settings

    global_settings.INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.contenttypes',
        'logical_rules',
        'logical_rules.tests.test_app'
    )
    if django.VERSION > (1,2):
        global_settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_PATH, 'connpass.sqlite'),
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        }
    else:
        global_settings.DATABASE_ENGINE = "sqlite3"
        global_settings.DATABASE_NAME = ":memory:"

    global_settings.ROOT_URLCONF = 'logical_rules.tests.test_app.urls'

    global_settings.MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    global_settings.SECRET_KEY = "blahblah"
    global_settings.DEBUG = True
    global_settings.TEMPLATE_DEBUG = True
    global_settings.SECRET_KEY = "guesswho"

    django.setup()

    from django.test.utils import get_runner
    test_runner = get_runner(global_settings)

    test_runner = test_runner()
    failures = test_runner.run_tests(['logical_rules',])

    sys.exit(failures)

if __name__ == '__main__':
    main()
