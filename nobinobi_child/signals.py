import logging
from sys import stdout

from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _

from nobinobi_child.models import Absence, Child

GROUP_NAME = getattr(settings, "GROUP_NAME_USERS", "Users")


def create_group_nobinobi_child(sender, **kwargs):
    absences_type = ContentType.objects.get_for_model(Absence)
    children_type = ContentType.objects.get_for_model(Child)

    group, created = Group.objects.get_or_create(name=('%s' % GROUP_NAME))
    if created:
        logging.info('%s Group created' % GROUP_NAME)
        stdout.write(_("Groups {} created successfully.").format(group))
        # Code to add permission to group ???
    permissions = [
        (absences_type, "add_absence"),
        (absences_type, "change_absence"),
        (absences_type, "delete_absence"),
        (absences_type, "view_absence"),
        (children_type, "view_child"),
    ]
    # Now what - Say I want to add 'Can add project' permission to new_group?
    permission_list = []
    for content_type, perm in permissions:
        permission_list.append(
            Permission.objects.get(content_type=content_type, codename=perm))

    for permission in permission_list:
        group.permissions.add(permission)
        stdout.write(_("Permission {} added to {} successfully.\n").format(permission, group))