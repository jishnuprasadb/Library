# Generated by Django 3.2.13 on 2022-07-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCollage', '0002_studentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='Teacher_Photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
