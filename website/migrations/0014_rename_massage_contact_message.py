# Generated by Django 3.2.19 on 2023-06-21 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_delete_newsletter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='massage',
        ),
    ]