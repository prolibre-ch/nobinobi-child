# from config.wsgi import logger
import arrow
from django.core.handlers.base import logger
from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

# from config.wsgi import logger
from nobinobi_child.models import Child
from nobinobi_child.models import LogChangeClassroom


class Command(BaseCommand):
    help = "Command for change classroom for child"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')
    def handle(self, *args, **options):
        logger.info(_("*** Launch of the change of school year task. ***"))

        # executing empty sample job
        children = Child.objects.filter(next_classroom__isnull=False, date_next_classroom__isnull=False)

        for child in children:
            # if child class =/= next_Classroom
            if child.classroom != child.next_classroom:
                # if date to change
                if child.date_next_classroom:
                    now_date = arrow.now().date()
                    if now_date >= child.date_next_classroom:
                        LogChangeClassroom.objects.create(child=child, classroom=child.classroom,
                                                          next_classroom=child.next_classroom,
                                                          date=now_date)
                        child.classroom = child.next_classroom
                        child.next_classroom = None
                        child.date_next_classroom = None

                        if child.status == Child.STATUS.future:
                            child.status = Child.STATUS.in_progress

                        child.save()
                        logger.info(_("The child {} changed school year.").format(child))
                else:
                    pass

        logger.info(_("*** End of the change of school year task. ***"))
