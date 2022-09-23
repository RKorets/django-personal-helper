from django import template
from contacts.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def count_contact(context):
    count = Contacts.objects.filter(user_id=context['request'].user.id).count()
    return count
