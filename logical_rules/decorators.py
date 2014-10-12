import logical_rules


def register_rule(rule_name=None):
    """
    A simple decorator for registering a logical rule. Instead of:

        def user_can_do_foo(user):
            return True

        logical_rules.register('user_can_do_foo', user_can_do_foo)

    You can just do this:

        @register_rule('can_foo')
        def user_can_do_foo(user):
            return True

    If you call `register_rule` with no arguments, the function
    name is re-used as the rule name.

        @register_rule()
        def user_can_do_foo(user):
            return True
    """
    def decorating(func):
        logical_rules.site.register(rule_name or func.__name__, func)
        return func
    return decorating
