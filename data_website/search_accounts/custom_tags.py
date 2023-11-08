from django import template

register = template.Library()


@register.filter
def ignore_form_error(field):
    """
    A filter that returns the field value if it exists and is not None,
    otherwise returns an empty string.
    """
    return field.value() if field and field.value() is not None else ""
