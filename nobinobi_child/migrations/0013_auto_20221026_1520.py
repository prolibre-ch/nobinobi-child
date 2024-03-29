# Generated by Django 3.2.11 on 2022-10-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0012_child_autorisations'),
    ]

    operations = [
        migrations.AddField(
            model_name='nobinobichildsettings',
            name='admin_child_list_display_order',
            field=models.CharField(choices=[('STD', 'Standard (First name, Last name)'), ('INV', 'Inverse (Last name, First Name')], default='STD', max_length=3),
        ),
        migrations.AddField(
            model_name='nobinobichildsettings',
            name='admin_child_ordering',
            field=models.CharField(choices=[('STD', 'Standard (First name, Last name)'), ('INV', 'Inverse (Last name, First Name')], default='STD', max_length=3),
        ),
    ]
