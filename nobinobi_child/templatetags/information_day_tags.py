# Here, register is a django.template.Library instance, as before
from django import template
from django.utils import timezone

from nobinobi_child.models import InformationOfTheDay

register = template.Library()


@register.inclusion_tag('nobinobi_child/includes/show_iotd.html', takes_context=True)
def show_iotd(context, count=100):
    # get iotd
    if context.request.user:
        iotds = InformationOfTheDay.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now(),
                                                   classrooms__allowed_login=context.request.user)
    else:
        iotds = []
    return {
        "iotds": iotds[:count],
    }
