from django import template
from contacts.models import *

register = template.Library()


@register.inclusion_tag('contacts/birthday_notification_template.html', takes_context=True)
def show_birthday(context):
    birthday_contact = Contacts.objects.filter(user_id=context['request'].user.id)
    data = []
    for contact in birthday_contact:
        if contact.days_to_birthday() != 'date is empty' and contact.days_to_birthday() < 8:
            data.append(contact)
    return {'birthdays': data}
