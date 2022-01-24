# Generated by Django 3.2.8 on 2022-01-19 09:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_rename_doctorprofile_doctorinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorinfo',
            old_name='PerPatientConsultancyDuration',
            new_name='ConsultancyDuration',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='Institute',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='specialist',
        ),
        migrations.AddField(
            model_name='qualification',
            name='InstituteName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='qualification',
            name='Specialist',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='About',
            field=models.TextField(blank=True, null=True),
        ),
    ]