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

# Generated by Django 2.2 on 2019-04-29 10:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import model_utils.fields
import nobinobi_child.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='absence',
            options={'ordering': ('start_date', 'end_date', 'child'), 'verbose_name': 'Absence', 'verbose_name_plural': 'Absences'},
        ),
        migrations.AlterModelOptions(
            name='absencegroup',
            options={'ordering': ('name',), 'verbose_name': 'Groupe d’absences', 'verbose_name_plural': 'Groupes d’absences'},
        ),
        migrations.AlterModelOptions(
            name='absencetype',
            options={'ordering': ('order', 'group', 'name'), 'verbose_name': "Type d'absence", 'verbose_name_plural': 'Types d’absences'},
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('country', 'zip', 'city', 'street'), 'verbose_name': 'Adresse', 'verbose_name_plural': 'Adresses'},
        ),
        migrations.AlterModelOptions(
            name='agegroup',
            options={'ordering': ('order', 'name'), 'verbose_name': "Groupe d'âge", 'verbose_name_plural': "Groupes d'âge"},
        ),
        migrations.AlterModelOptions(
            name='allergy',
            options={'ordering': ('name',), 'verbose_name': 'Allergie', 'verbose_name_plural': 'Allergies'},
        ),
        migrations.AlterModelOptions(
            name='child',
            options={'ordering': ('first_name', 'last_name', 'created'), 'verbose_name': 'Enfant', 'verbose_name_plural': 'Enfants'},
        ),
        migrations.AlterModelOptions(
            name='childspecificneed',
            options={'ordering': ('child',), 'verbose_name': 'Besoins spécifiques de l’enfant', 'verbose_name_plural': 'Enfants à besoins spécifiques'},
        ),
        migrations.AlterModelOptions(
            name='childtocontact',
            options={'ordering': ('child', 'order'), 'verbose_name': 'Enfant vers contact', 'verbose_name_plural': 'Enfants aux contacts'},
        ),
        migrations.AlterModelOptions(
            name='childtoperiod',
            options={'ordering': ('start_date', 'end_date', 'child', 'period'), 'verbose_name': 'Enfant vers période', 'verbose_name_plural': 'Enfants aux périodes'},
        ),
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ('order', 'name'), 'verbose_name': 'Salle de classe', 'verbose_name_plural': 'Salles de classes'},
        ),
        migrations.AlterModelOptions(
            name='classroomdayoff',
            options={'ordering': ('weekday',), 'verbose_name': 'Jour de congé', 'verbose_name_plural': 'Jours de congés'},
        ),
        migrations.AlterModelOptions(
            name='foodrestriction',
            options={'ordering': ('name',), 'verbose_name': 'Restriction alimentaire', 'verbose_name_plural': 'Restrictions alimentaires'},
        ),
        migrations.AlterModelOptions(
            name='informationoftheday',
            options={'ordering': ('start_date', 'end_date'), 'verbose_name': 'Information du jour', 'verbose_name_plural': 'Informations des jours'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('name', 'created'), 'verbose_name': 'Langue', 'verbose_name_plural': 'Langues'},
        ),
        migrations.AlterModelOptions(
            name='logchangeclassroom',
            options={'ordering': ('date',), 'verbose_name': 'Journal de changement de classe', 'verbose_name_plural': 'Journaux de changement de classe'},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ('weekday', 'order', 'name'), 'verbose_name': 'Période', 'verbose_name_plural': 'Périodes'},
        ),
        migrations.RemoveField(
            model_name='absence',
            name='date',
        ),
        migrations.RemoveField(
            model_name='childtoperiod',
            name='date',
        ),
        migrations.RemoveField(
            model_name='informationoftheday',
            name='date',
        ),
        migrations.AddField(
            model_name='absence',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 10, 3, 33, 847499, tzinfo=utc), verbose_name='Date de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='absence',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 10, 3, 38, 919489, tzinfo=utc), verbose_name='Date de début'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtoperiod',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 10, 3, 48, 7786, tzinfo=utc), verbose_name='Date de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtoperiod',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 10, 3, 48, 7786, tzinfo=utc), verbose_name='Date de début'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informationoftheday',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 10, 3, 55, 319308, tzinfo=utc), verbose_name='Date de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informationoftheday',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 10, 4, 0, 424127, tzinfo=utc), verbose_name='Date de début'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='absence',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.AbsenceType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='absencetype',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.AbsenceGroup', verbose_name='Groupe'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='Suisse', max_length=50, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='child',
            name='age_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nobinobi_child.AgeGroup', verbose_name="Groupe d'âge"),
        ),
        migrations.AlterField(
            model_name='child',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='child',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom', to='nobinobi_child.Classroom', verbose_name='Salle de classe'),
        ),
        migrations.AlterField(
            model_name='child',
            name='date_next_classroom',
            field=models.DateField(blank=True, null=True, verbose_name='Date prochaine salle de classe'),
        ),
        migrations.AlterField(
            model_name='child',
            name='food_restrictions',
            field=models.ManyToManyField(blank=True, related_name='food_restrictions', to='nobinobi_child.FoodRestriction', verbose_name='Restrictions alimentaires'),
        ),
        migrations.AlterField(
            model_name='child',
            name='languages',
            field=models.ManyToManyField(related_name='languages', to='nobinobi_child.Language', verbose_name='Langues'),
        ),
        migrations.AlterField(
            model_name='child',
            name='next_classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_classroom', to='nobinobi_child.Classroom', verbose_name='Prochaine salle de classe'),
        ),
        migrations.AlterField(
            model_name='child',
            name='periods',
            field=models.ManyToManyField(blank=True, related_name='periods', through='nobinobi_child.ChildToPeriod', to='nobinobi_child.Period', verbose_name='Périodes'),
        ),
        migrations.AlterField(
            model_name='child',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=nobinobi_child.models.Child.upload_picture_child, verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='child',
            name='red_list',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Liste rouge'),
        ),
        migrations.AlterField(
            model_name='child',
            name='renewal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de renouvellement'),
        ),
        migrations.AlterField(
            model_name='child',
            name='usual_name',
            field=models.CharField(max_length=100, verbose_name='Nom usuel'),
        ),
        migrations.AlterField(
            model_name='childspecificneed',
            name='attachment',
            field=models.FileField(upload_to=nobinobi_child.models.ChildSpecificNeed.upload_attachment_child, verbose_name='Pièce jointe'),
        ),
        migrations.AlterField(
            model_name='childspecificneed',
            name='child',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='childspecificneed',
            name='ihp',
            field=models.BooleanField(default=True, verbose_name="Project d'accueil individualisé"),
        ),
        migrations.AlterField(
            model_name='childspecificneed',
            name='measure_take',
            field=model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Mesure à prendre'),
        ),
        migrations.AlterField(
            model_name='childspecificneed',
            name='problem',
            field=model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Problème'),
        ),
        migrations.AlterField(
            model_name='childtocontact',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='childtocontact',
            name='link_with_child',
            field=models.CharField(help_text='Type contact: Exemple Père, Mère ...', max_length=50, verbose_name="Lien avec l'enfant"),
        ),
        migrations.AlterField(
            model_name='childtoperiod',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='childtoperiod',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Period', verbose_name='Période'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='allowed_login',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Connexion autorisée'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='capacity',
            field=models.PositiveIntegerField(default=20, verbose_name='Capacité'),
        ),
        migrations.AlterField(
            model_name='classroomdayoff',
            name='classrooms',
            field=models.ManyToManyField(to='nobinobi_child.Classroom', verbose_name='Salle de classe'),
        ),
        migrations.AlterField(
            model_name='classroomdayoff',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')], verbose_name='Jour de la semaine'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.Address', verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='function',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Fonction'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='professional_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Téléphone professionnel'),
        ),
        migrations.AlterField(
            model_name='informationoftheday',
            name='classrooms',
            field=models.ManyToManyField(related_name='classrooms', to='nobinobi_child.Classroom', verbose_name='Salle de classe'),
        ),
        migrations.AlterField(
            model_name='informationoftheday',
            name='content',
            field=model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='logchangeclassroom',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='logchangeclassroom',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_change_classroom', to='nobinobi_child.Classroom', verbose_name='Salle de classe'),
        ),
        migrations.AlterField(
            model_name='logchangeclassroom',
            name='next_classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_change_next_classroom', to='nobinobi_child.Classroom', verbose_name='Prochaine salle de classe'),
        ),
        migrations.AlterField(
            model_name='period',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')], verbose_name='Jour de la semaine'),
        ),
    ]
