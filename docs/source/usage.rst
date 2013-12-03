.. _ref-usage:

Usage
=====

Template Tags
*************

Once you have created a rule, it's easy to use anywhere in your templates::

	{% load logical_rules_tags %}
	{% testrule user_can_edit_mymodel object request.user %}
		<p>You are the owner!</p>
	{% endtestrule %}
	
**Note:** *Don't use quotes around the rule name in the template.*

Direct Calling
**************

::

	import logical_rules
	if logical_rules.site.test_rule(rule['name'], arg1, arg2):
		print "passed"
	else:
		print "failed"
		
RulesMixin
**********

If you are extending `Django's class-based generic views`__, you might find this mixin useful. It allows you to define rules that should be applied before rendering a view. Here's an example usage::

   class MyView(RulesMixin, DetailView):

      def update_logical_rules(self):
         super(MyView, self).update_logical_rules()
         self.add_logical_rule({
            'name': 'user_can_edit_mymodel',
            'param_callbacks': [
               ('object', 'get_object'),
               ('user', 'get_request_user')
            ]
         })

``param_callbacks`` are our technique for getting the parameters for your rule. These are assumed to be methods on your class. ``get_request_user()`` is defined in RuleMixin since it's so common. ``get_object()`` is a method on the DetailView class.

Rule dictionaries can have other properties, like ``redirect_url`` and ``response_callback``. If ``redirect_url`` is defined, then the view will return an ``HttpResponseRedirect`` to that URL. If ``response_callback`` is defined, then the view will return the result of that method.

Messaging integration is possible with ``message`` and ``message_level`` options.

Finally, we've added two commonly used rules. As an optional substitute for ``login_required``, we have ``user_is_authenticated`` and to test a generic expression, we have ``evaluate_expression``.

.. _DjangoGenericViews: https://docs.djangoproject.com/en/dev/topics/class-based-views/

__ DjangoGenericViews_