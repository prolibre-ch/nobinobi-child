# Generated by Django 3.2.11 on 2022-05-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0008_childtrackinglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='date_end_child',
            field=models.DateField(blank=True, help_text='When this field is filled and saved, all period equal/after this date will be set to this date and child will be archived at this date.', null=True, verbose_name='Date end for child'),
        ),
    ]
