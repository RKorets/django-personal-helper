from django import template
from files.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def count_files(context):
    count = Files.objects.filter(user=context['request'].user).count()
    return count
