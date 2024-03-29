# Generated by Django 3.2.23 on 2024-02-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0015_auto_20231103_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='nobinobichildsettings',
            name='admin_child_absence_ordering',
            field=models.CharField(choices=[('STD', 'Standard (Start date, End date, Child)'), ('CH', 'Child (Last name, Start date, End date')], default='STD', max_length=3, verbose_name='Admin child absence ordering'),
        ),
    ]
