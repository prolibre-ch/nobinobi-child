# -*- coding: utf-8
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class NobinobiChildConfig(AppConfig):
    name = 'nobinobi_child'

    def ready(self):
        from nobinobi_child.signals import create_group_nobinobi_child
        post_migrate.connect(create_group_nobinobi_child, sender=self)
