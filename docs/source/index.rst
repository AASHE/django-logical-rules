django-logical-rules
====================

When you need logic...

A tool to manage logical rules throughout your application. Logical rules are more powerful than permission or rule tables because they are written in python. Register a rule once and work with it throughout your app, from templates to generic view mixins. Instead of cluttering your models with rule-style and permission-style methods define those rules in rules.py and then get easy access to them in your views and templates.

.. toctree::
	:maxdepth: 2
	
	usage
	tutorial

Installation
************

Use pip to install from PyPI::

    pip install django-logical-rules

Add ``storages`` to your settings.py file::

    INSTALLED_APPS = (
        ...
        'django-logical-rules',
        ...
    )

If you want to use the messaging features, install `Django messages framework`__.

rules.py
********

Simply add **rules.py** to your app and use them throughout your app. Here's what a rule looks like::

	import logical_rules

	def user_can_edit_mymodel(object, user):
		"""
			Confirms a user can edit a specific model
			...owners only!
		"""
		return object.owner == user
	logical_rules.site.register("user_can_edit_mymodel", user_can_edit_mymodel)

Configuration
*************

To include your models in the registry you will need to do run the autodiscover, a bit like django.contrib.admin (I generally put this in my **urls.py**)::

	import logical_rules
	logical_rules.autodiscover()
	
Performance
***********

Performance varies mainly around how you write your rules. Often it's a good idea to use caching in your rules when a permission isn't changing frequently.

Contributing
************

Think this needs something else? To contribute to ``django-logical-rules`` create a fork on Bitbucket_. Clone your fork, make some changes, and submit a pull request.

Bugs are great contributions too! Feel free to add an issue on Bitbucket_:

.. _Bitbucket: https://bitbucket.org/aashe/django-logical-rules 

.. _DjangoMessaging: https://docs.djangoproject.com/en/dev/ref/contrib/messages/

__ DjangoMessaging_
