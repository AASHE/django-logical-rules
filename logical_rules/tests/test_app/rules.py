import logical_rules

from logical_rules.decorators import register_rule

def test_is_pizza(word):
    if word == "pizza":
        return True
    return False
logical_rules.site.register("test_is_pizza", test_is_pizza)


@register_rule()
def test_is_hamburger(word):
    "Rule using register_rule with no args"
    return word == 'hamburger'


@register_rule('test_is_even')
def test_modulo_two(number):
    "Rule using register_rule with custom name"
    return number % 2 == 0
