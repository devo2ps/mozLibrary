# Generated by Django 2.2.6 on 2019-11-01 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20191101_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_final', 'Set book as something'),)},
        ),
    ]
