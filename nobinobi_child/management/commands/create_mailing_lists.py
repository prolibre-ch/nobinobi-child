# from config.wsgi import logger
from django.core.handlers.base import logger
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.utils.translation import gettext as _

from nobinobi_child.models import Child, Classroom, AgeGroup, ChildToContact
import csv

def write_csv_from_children(children, date, type):
    type = str(type)
    with open('mailing_lists_{}_{}.csv'.format(type, date), mode='w', encoding="UTF8") as csv_file:
        fieldnames = ['email', 'first_name', 'last_name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for child in children:
            ctc_parents = ChildToContact.objects.filter(child=child)
            for ctc_contact in ctc_parents:
                contact = ctc_contact.contact
                if contact.email:
                    writer.writerow(
                        {'email': contact.email, 'first_name': contact.first_name, 'last_name': contact.last_name})


class Command(BaseCommand):
    help = _("Command for create a mailing lists of parents.")

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--all',
            type=str,
            help=_(
                "--all all for all child")
        )
        parser.add_argument(
            '--classroom',
            type=str,
            help=_(
                "--classroom classroom_name for child in this classroom.")
        )
        parser.add_argument(
            '--age-group',
            type=str,
            help=_(
                "--age-group age_group_name for child in this age group.")
        )

    def handle(self, *args, **options):
        logger.info(_("*** Launch of create a mailing lists of parents task. ***"))
        self.stdout.write(self.style.SUCCESS(_("*** Launch of create a mailing lists of parents task. ***")))
        all = options['all']
        classroom = options['classroom']
        age_group = options['age_group']
        date = timezone.localdate()
        if all == "all":
            children = Child.objects.filter(status__exact=Child.STATUS.in_progress)
            self.stdout.write(self.style.SUCCESS(_("*** Options : all ***")))
            # create the csv
            write_csv_from_children(children, date, all)

        if classroom:
            try:
                classroom = Classroom.objects.get(name__iexact=classroom)
                self.stdout.write(self.style.SUCCESS(_("*** Options : Classroom ***")))
            except Classroom.DoesNotExist:
                raise CommandError('Classroom "%s" does not exist' % classroom)

            children = Child.objects.filter(status__exact=Child.STATUS.in_progress, classroom=classroom)
            write_csv_from_children(children, date, classroom)

        if age_group:
            try:
                age_group = AgeGroup.objects.get(name__iexact=age_group)
                self.stdout.write(self.style.SUCCESS(_("*** Options : Age group ***")))
            except AgeGroup.DoesNotExist:
                raise CommandError(_('Age group "{}" does not exist').format(age_group))

            children = Child.objects.filter(status__exact=Child.STATUS.in_progress,
                                            age_group=age_group)
            write_csv_from_children(children, date, age_group)

        if not all and not age_group and not classroom:
            raise CommandError(_('No option selected'))

        self.stdout.write(self.style.SUCCESS(_("*** End of create a mailing lists of parents task. ***")))
        logger.info(_("*** End of create a mailing lists of parents task.. ***"))
