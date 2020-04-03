# Generated by Django 2.2 on 2019-04-23 09:25

from django.conf import settings
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import nobinobi_child.models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nobinobi_staff', '0006_staff_working_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Absence group',
                'verbose_name_plural': 'Absence groups',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('street', models.CharField(max_length=100, verbose_name='Rue')),
                ('zip', models.PositiveIntegerField(verbose_name='Nip')),
                ('city', models.CharField(max_length=50, verbose_name='Ville')),
                ('country', models.CharField(default='Switzerland', max_length=50, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'ordering': ('country', 'zip', 'city', 'street'),
            },
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Ordre')),
            ],
            options={
                'verbose_name': 'Age group',
                'verbose_name_plural': 'Age groups',
                'ordering': ('order', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Allergy',
                'verbose_name_plural': 'Allergies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('in_progress', 'In progress'), ('archived', 'Archived'), ('future', 'Future')], default='in_progress', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom de famille')),
                ('usual_name', models.CharField(max_length=100, verbose_name='Usual name')),
                ('gender', model_utils.fields.StatusField(choices=[('boy', 'Boy'), ('girl', 'Girl'), ('other', 'Autre')], default='boy', max_length=100, no_check_for_status=True, null=True, verbose_name='Sexe')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=nobinobi_child.models.Child.upload_picture_child, verbose_name='Picture')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('red_list', models.CharField(blank=True, max_length=255, null=True, verbose_name='Red list')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Commentaire')),
                ('renewal_date', models.DateField(blank=True, null=True, verbose_name='Renewal date')),
                ('date_next_classroom', models.DateField(blank=True, null=True, verbose_name='Date next classroom')),
                ('age_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nobinobi_child.AgeGroup', verbose_name='Age group')),
                ('allergies', models.ManyToManyField(blank=True, related_name='allergies', to='nobinobi_child.Allergy', verbose_name='Allergies')),
            ],
            options={
                'verbose_name': 'Child',
                'verbose_name_plural': 'Children',
                'ordering': ('first_name', 'last_name', 'created'),
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nom')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Ordre')),
                ('capacity', models.PositiveIntegerField(default=20, verbose_name='Capacity')),
                ('mode', model_utils.fields.StatusField(choices=[('creche', 'Creche'), ('kindergarten', 'Kindergarten')], default='creche', max_length=15, no_check_for_status=True, verbose_name='Mode')),
                ('allowed_login', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Allowed login')),
            ],
            options={
                'verbose_name': 'Classroom',
                'verbose_name_plural': 'Classrooms',
                'ordering': ('order', 'name'),
            },
        ),
        migrations.CreateModel(
            name='FoodRestriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Food restriction',
                'verbose_name_plural': 'Food restrictions',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ('name', 'created'),
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('weekday', models.IntegerField(choices=[(1, 'lundi'), (2, 'mardi'), (3, 'mercredi'), (4, 'jeudi'), (5, 'vendredi'), (6, 'samedi'), (7, 'dimanche')], verbose_name='Weekday')),
                ('order', models.PositiveIntegerField(verbose_name='Ordre')),
            ],
            options={
                'verbose_name': 'Period',
                'verbose_name_plural': 'Periods',
                'ordering': ('weekday', 'order', 'name'),
                'unique_together': {('weekday', 'order')},
            },
        ),
        migrations.CreateModel(
            name='InformationOfTheDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text='Date time range for information', verbose_name='Date')),
                ('content', model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Content')),
                ('_content_excerpt', models.TextField(editable=False)),
                ('classrooms', models.ManyToManyField(related_name='classrooms', to='nobinobi_child.Classroom', verbose_name='Classroom')),
            ],
            options={
                'verbose_name': 'Information of the day',
                'verbose_name_plural': 'Information of the days',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom de famille')),
                ('email', models.EmailField(max_length=254, verbose_name='Courriel')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Téléphone')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Téléphone portable')),
                ('professional_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Professional phone')),
                ('organisation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organisation')),
                ('function', models.CharField(blank=True, max_length=100, null=True, verbose_name='Function')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.Address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='ClassroomDayOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('weekday', models.IntegerField(choices=[(1, 'lundi'), (2, 'mardi'), (3, 'mercredi'), (4, 'jeudi'), (5, 'vendredi'), (6, 'samedi'), (7, 'dimanche')], verbose_name='Weekday')),
                ('classrooms', models.ManyToManyField(to='nobinobi_child.Classroom', verbose_name='Classroom')),
            ],
            options={
                'verbose_name': 'Classroom day off',
                'verbose_name_plural': 'Classrooms days off',
                'ordering': ('weekday',),
            },
        ),
        migrations.CreateModel(
            name='ChildToPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField(help_text='Date range for period', verbose_name='Date')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Child')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Period', verbose_name='Period')),
            ],
            options={
                'verbose_name': 'Child to period',
                'verbose_name_plural': 'Children to periods',
                'ordering': ('date', 'child', 'period'),
            },
        ),
        migrations.CreateModel(
            name='ChildToContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('link_with_child', models.CharField(help_text='Type contact: Exemple Père, Mère etc...', max_length=50, verbose_name='Link with child')),
                ('order', models.PositiveIntegerField(verbose_name='Ordre')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Child')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Contact', verbose_name='Contact')),
            ],
            options={
                'verbose_name': 'Child to contact',
                'verbose_name_plural': 'Children to contacts',
                'ordering': ('child', 'order'),
            },
        ),
        migrations.CreateModel(
            name='ChildSpecificNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('problem', model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Problem')),
                ('ihp', models.BooleanField(default=True, verbose_name='Individual home project')),
                ('attachment', models.FileField(upload_to=nobinobi_child.models.ChildSpecificNeed.upload_attachment_child, verbose_name='Attachment')),
                ('measure_take', model_utils.fields.SplitField(no_excerpt_field=True, verbose_name='Measure to take')),
                ('_problem_excerpt', models.TextField(editable=False)),
                ('_measure_take_excerpt', models.TextField(editable=False)),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Child')),
            ],
            options={
                'verbose_name': 'Child specific need',
                'verbose_name_plural': 'Children specific needs',
                'ordering': ('child',),
            },
        ),
        migrations.AddField(
            model_name='child',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom', to='nobinobi_child.Classroom', verbose_name='Classroom'),
        ),
        migrations.AddField(
            model_name='child',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='contacts', through='nobinobi_child.ChildToContact', to='nobinobi_child.Contact', verbose_name='Contacts'),
        ),
        migrations.AddField(
            model_name='child',
            name='food_restrictions',
            field=models.ManyToManyField(blank=True, related_name='food_restrictions', to='nobinobi_child.FoodRestriction', verbose_name='Food restrictions'),
        ),
        migrations.AddField(
            model_name='child',
            name='languages',
            field=models.ManyToManyField(related_name='languages', to='nobinobi_child.Language', verbose_name='Languages'),
        ),
        migrations.AddField(
            model_name='child',
            name='next_classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_classroom', to='nobinobi_child.Classroom', verbose_name='Next classroom'),
        ),
        migrations.AddField(
            model_name='child',
            name='periods',
            field=models.ManyToManyField(blank=True, related_name='periods', through='nobinobi_child.ChildToPeriod', to='nobinobi_child.Period', verbose_name='Periods'),
        ),
        migrations.AddField(
            model_name='child',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nobinobi_staff.Staff', verbose_name='Personnel'),
        ),
        migrations.CreateModel(
            name='AbsenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('order', models.PositiveIntegerField(verbose_name='Ordre')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.AbsenceGroup', verbose_name='Group')),
            ],
            options={
                'verbose_name': "Type d'absence",
                'verbose_name_plural': 'Absence types',
                'ordering': ('order', 'group', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text='Start date to end date', verbose_name='Date')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Child')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nobinobi_child.AbsenceType', verbose_name='AbsenceType')),
            ],
            options={
                'verbose_name': 'Absence',
                'verbose_name_plural': 'Absences',
                'ordering': ('date', 'child'),
            },
        ),
        migrations.CreateModel(
            name='LogChangeClassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField(verbose_name='Date')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_child.Child', verbose_name='Child')),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_change_classroom', to='nobinobi_child.Classroom', verbose_name='Classroom')),
                ('next_classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_change_next_classroom', to='nobinobi_child.Classroom', verbose_name='Next classroom')),
            ],
            options={
                'verbose_name': 'Log change classroom',
                'verbose_name_plural': 'Logs changed classrooms',
                'ordering': ('date',),
                'unique_together': {('child', 'classroom')},
            },
        ),
    ]
