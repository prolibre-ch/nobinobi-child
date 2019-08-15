from django.core.management.base import BaseCommand
from nobinobi_child.jobs.daily.change_auto_agegroup import Job


class Command(BaseCommand):
    help = "Command for set agegroup auto"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')
    def handle(self, *args, **options):
        Job.execute()
