# Generated by Django 5.0.3 on 2024-03-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisees', '0002_subject_subjectarea'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
