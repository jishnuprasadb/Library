# Generated by Django 4.1.1 on 2022-10-25 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course_Fees',
            new_name='Course_Fee',
        ),
    ]
