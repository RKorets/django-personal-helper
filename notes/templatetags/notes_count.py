from django import template
from notes.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def count_notes(context):
    count = Note.objects.filter(user_id=context['request'].user.id).count()
    return count
