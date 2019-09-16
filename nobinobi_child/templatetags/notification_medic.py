from django.template.defaulttags import register


@register.inclusion_tag('notifications/medic.html', takes_context=True)
def include_notif(context):
    import importlib
    spam_spec = importlib.util.find_spec("nobinobi_daily_follow_up")
    found = spam_spec is not None
    if found:
        dfu = True
    else:
        dfu = False
    return {
        "dfu": dfu
    }
