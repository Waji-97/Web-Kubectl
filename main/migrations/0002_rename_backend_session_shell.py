# Generated by Django 5.0.2 on 2024-02-24 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='backend',
            new_name='shell',
        ),
    ]