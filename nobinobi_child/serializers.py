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
from rest_framework import serializers

from nobinobi_child.models import Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ChildSerializer, self).to_representation(instance)
        representation['gender'] = instance.get_gender_display()
        representation['picture'] = instance.picture.url if instance.picture else None
        representation['birth_date'] = instance.birth_date if instance.birth_date else "-"
        representation['classroom'] = instance.classroom.name if instance.classroom else "-"
        representation['age_group'] = instance.age_group.name if instance.age_group else "-"
        representation['staff'] = instance.staff.full_name if instance.staff else "-"
        return representation
