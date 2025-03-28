from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiply two numbers and return the result."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0