# Generated by Django 3.2.11 on 2023-02-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0013_auto_20221026_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='nobinobichildsettings',
            name='default_menu',
            field=models.BooleanField(default=True),
        ),
    ]