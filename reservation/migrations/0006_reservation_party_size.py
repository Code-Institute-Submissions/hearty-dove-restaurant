# Generated by Django 3.2.13 on 2022-06-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reservation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='party_size',
            field=models.IntegerField(default=1),
        ),
    ]
