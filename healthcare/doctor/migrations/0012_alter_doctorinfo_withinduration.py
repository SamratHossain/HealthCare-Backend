# Generated by Django 3.2.8 on 2022-01-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_alter_qualification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='WithinDuration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
