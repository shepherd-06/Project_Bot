# Generated by Django 2.0.4 on 2018-05-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank', '0006_auto_20180509_0258'),
    ]
    operations = [
        migrations.AlterField(
            model_name='flowcontroller',
            name='expirationDate',
            field=models.DateTimeField(verbose_name='Request Expiration Date'),
        ),
    ]
