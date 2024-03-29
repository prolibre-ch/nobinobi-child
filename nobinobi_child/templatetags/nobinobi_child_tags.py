#  Copyright (C) 2020 <Florian Alu - Prolibre - https://prolibre.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Here, register is a django.template.Library instance, as before
from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row as django_submit_row

register = template.Library()


@register.filter
def startswith(value, arg):
    """Usage, {% if value|starts_with:"arg" %}"""
    return value.startswith(arg)


@register.inclusion_tag('admin/nobinobi_child/child/submit_line.html', takes_context=True)
def submit_row_custom(context):
    """
    Currently only way of overriding Django admin submit_line.html is by replacing
    submit_row template tag in change_form.html
    """
    return django_submit_row(context)
