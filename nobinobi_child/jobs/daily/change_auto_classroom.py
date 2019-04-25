import arrow
from django.core.handlers.base import logger
from django_extensions.management.jobs import DailyJob
from django.utils.translation import gettext as _
# from config.wsgi import logger
from nobinobi_child.models import Child, LogChangeClassroom


class Job(DailyJob):
    help = _("Change of school year")

    def execute(self):
        logger.info(_("*** Launch of the change of school year task. ***"))

        # executing empty sample job
        children = Child.objects.filter(next_classroom__isnull=False, next_classroom_date__isnull=False)

        for child in children:
            # if child class =/= next_Classroom
            if child.classroom != child.prochaine_classe:
                # if date to change
                if child.prochaine_classe_date:
                    now_date = arrow.now().date()
                    if now_date >= child.prochaine_classe_date:
                        LogChangeClassroom.objects.create(child=child, classroom=child.classroom,
                                                           next_classroom=child.next_classroom,
                                                           date_changement=now_date)
                        child.classroom = child.next_classroom
                        child.next_classroom = None
                        child.next_classroom_date = None

                        if child.status == Child.STATUS.future:
                            child.status = Child.STATUS.in_progress

                        child.save()
                        logger.info(_("The child {} changed school year.").format(child))
                else:
                    pass

        logger.info(_("*** End of the change of school year task. ***"))
