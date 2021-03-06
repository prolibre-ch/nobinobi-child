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

# Generated by Django 2.2 on 2019-06-04 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0004_auto_20190531_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='allowed_login',
            field=models.ManyToManyField(related_name='classroom_login', to=settings.AUTH_USER_MODEL, verbose_name='Connexion autorisée'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.Address', verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Courriel'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Téléphone portable'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='professional_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Téléphone professionnel'),
        ),
        migrations.AlterField(
            model_name='period',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='Heure de fin'),
        ),
        migrations.AlterField(
            model_name='period',
            name='max_child',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Max enfant'),
        ),
        migrations.AlterField(
            model_name='period',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='Heure de début'),
        ),
    ]
