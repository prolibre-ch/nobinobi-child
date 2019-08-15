from django.core import management
from django.utils.translation import gettext as _
from django_extensions.management.jobs import DailyJob


# from config.wsgi import logger


class Job(DailyJob):
    help = _("Change of school year")

    def execute(self):
        management.call_command("change_agegroup_auto")
