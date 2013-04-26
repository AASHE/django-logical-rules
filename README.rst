====================
django-logical-rules
====================

A tool to manage logical rules throughout your application. Logical rules are more powerful than permission or rule tables because they are written in python. Register a rule once and work with it throughout your app, from templates to generic view mixins. Instead of cluttering your models with rule-style and permission-style methods define those rules in **rules.py** and then get easy access to them in your views and templates.

Installation
============

Use ``pip`` to install from PyPI::

	pip install django-logical-rules

Add ``logical_rules`` to your settings.py file::

	INSTALLED_APPS = (
	    ...
	    'logical_rules',
	    ...
	)

Additional Requirements
=======================

If you want to use the messaging features install `Django messages framework`__.

Configuration
=============

Rules are defined in **rules.py** files within your apps. Here's an example of a rule::

	import logical_rules

	def user_can_edit_mymodel(mymodel, user):
		"""
			Confirms a user can edit a specific model
			...owners only!
		"""
		return mymodel.owner == user
	logical_rules.site.register("user_can_edit_mymodel", user_can_edit_mymodel)
	
To include your models in the registry you will need to do run the autodiscover, a bit like django.contrib.admin (I generally put this in **urls.py**)::

	import logical_rules
	logical_rules.autodiscover()


Usage
=====

Template Tag
------------

Once you have created a rule, it's easy to use anywhere in your templates::

	{% load logical_rules_tags %}
	{% testrule user_can_edit_mymodel object request.user %}
		<p>You are the owner!</p>
	{% endtestrule %}
	
**Note:** *Don't use quotes around the rule name in the template.*

RulesMixin
----------

If you are extending Django's class-based generic views, you might find this mixin useful. It allows you to define rules that should be applied before rendering a view. Here's an example usage::

	class MyView(RulesMixin, DetailView):

		def update_logical_rules(self):
			super(MyView, self).update_logical_rules()
			self.add_logical_rule({
				'name': 'user_can_edit_mymodel',
				'param_callbacks':
					[('get_request_user', 'get_object')],
			})

``param_callbacks`` are our technique for getting the parameters for your rule. These are assumed to be methods on your class. ``get_request_user()`` is defined in RuleMixin since it's so common. ``get_object()`` is a method on the DetailView class.

Rule dictionaries can have other properties, like ``redirect_url`` and ``response_callback``. If ``redirect_url`` is defined, then the view will return an ``HttpResponseRedirect`` to that URL. If ``response_callback`` is defined, then the view will return the result of that method.

Messaging integration is possible with ``message`` and ``message_level`` options.

Finally, we've added two commonly used rules. As an optional substitute for ``login_required``, we have ``user_is_authenticated`` and to test a generic expression, we have ``evaluate_expression``.

Direct Calling
--------------

::

	import logical_rules
	if logical_rules.site.test_rule(rule['name'], arg1, arg2):
		print "passed"
	else:
		print "failed"

Contributing
============

Think this needs something else? To contribute to ``django-logical-rules`` create a fork on Bitbucket_. Clone your fork, make some changes, and submit a pull request.

Bugs are great contributions too! Feel free to add an issue on Bitbucket_:

.. _Bitbucket: https://bitbucket.org/aashe/django-logical-rules 

.. _DjangoMessaging: https://docs.djangoproject.com/en/dev/ref/contrib/messages/

__ DjangoMessaging_