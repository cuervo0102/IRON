# Generated by Django 4.2.5 on 2023-09-11 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_alter_sellerregistration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerregistration',
            name='user',
        ),
    ]
