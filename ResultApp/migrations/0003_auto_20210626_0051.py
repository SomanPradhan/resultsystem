# Generated by Django 3.2.4 on 2021-06-25 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0002_auto_20210626_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentclass',
            old_name='student',
            new_name='students',
        ),
        migrations.RenameField(
            model_name='studentsubject',
            old_name='students',
            new_name='student',
        ),
    ]
