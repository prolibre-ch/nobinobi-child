#      Copyright (C) Prolibre Sarl 2019 <Florian Alu> <alu@prolibre.com>
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License and any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
import arrow
import pytz
from django.conf import settings
from rest_framework import serializers

from nobinobi_child.models import Child, Absence, ChildToContact, ChildSpecificNeed


class ChildToContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildToContact
        fields = ('order', 'contact', 'link_with_child')
        depth = 1


class ChildSpecificNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildSpecificNeed
        fields = '__all__'


class ChildSerializer(serializers.ModelSerializer):
    # contacts = ContactSerializer(many=True)

    childtocontact_set = serializers.SerializerMethodField()
    childspecificneed = ChildSpecificNeedSerializer(read_only=True)

    class Meta:
        model = Child
        fields = '__all__'
        depth = 2

    def get_childtocontact_set(self, instance):
        songs = instance.childtocontact_set.all().order_by('order')
        return ChildToContactSerializer(songs, many=True).data

    def to_representation(self, instance):
        representation = super(ChildSerializer, self).to_representation(instance)
        representation['gender'] = instance.get_gender_display()
        representation['picture'] = instance.picture.url if instance.picture else None
        representation['birth_date'] = arrow.get(instance.birth_date).format("DD.MM.YYYY",
                                                                             locale="fr_fr") if instance.birth_date else "-"
        representation['classroom'] = instance.classroom.name if instance.classroom else "-"
        representation['age_group'] = instance.age_group.name if instance.age_group else "-"
        representation['staff'] = instance.staff.full_name if instance.staff else "-"
        representation['renewal_date'] = arrow.get(instance.renewal_date).format("DD.MM.YYYY", locale="fr_fr")

        return representation


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(AbsenceSerializer, self).to_representation(instance)
        format = "%d.%m.%Y %H:%M"
        local_timezone = pytz.timezone(getattr(settings, 'TIME_ZONE', None))
        representation['child'] = instance.child.full_name
        representation['start_date'] = instance.start_date.astimezone(local_timezone).strftime(format)
        representation['end_date'] = instance.end_date.astimezone(local_timezone).strftime(format)
        representation['type'] = "{0} ({1})".format(instance.type.name, instance.type.group.name)
        return representation
