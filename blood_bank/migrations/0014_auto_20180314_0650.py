# Generated by Django 2.0.1 on 2018-03-14 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank', '0013_auto_20180314_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstatus',
            old_name='donationAvail',
            new_name='donationAvailDate',
        ),
    ]
