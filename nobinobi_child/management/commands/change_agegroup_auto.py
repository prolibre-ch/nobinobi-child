import datetime

import arrow
from django.core.handlers.base import logger
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.translation import gettext as _

# from config.wsgi import logger
from nobinobi_child.models import AgeGroup, Child


class Command(BaseCommand):
    help = "Command for set agegroup auto"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')
    def handle(self, *args, **options):
        logger.info(_("*** Launch of the change of age group year task. ***"))
        now_date = timezone.localtime().date()
        age_groups = AgeGroup.objects.all()
        now_year = now_date.year
        for age_group in age_groups:
            if now_date == datetime.datetime.strptime("31/07/{}".format(now_year), "%d/%m/%Y"):
                age_group.from_date = arrow.get(age_group.from_date).shift(years=+1).date()
                age_group.end_date = arrow.get(age_group.end_date).shift(years=+1).date()
                age_group.save()

        # executing empty sample job
        children = Child.objects.exclude(status=Child.STATUS.archived)
        for child in children:
            if child.birth_date:
                new_age_group = AgeGroup.objects.filter(from_date__lte=child.birth_date,
                                                        end_date__gte=child.birth_date).first()
                child.age_group = new_age_group
                child.save()
                logger.info(_("The child {} changed age group.").format(child))

        logger.info(_("*** End of the change of age group year task. ***"))
