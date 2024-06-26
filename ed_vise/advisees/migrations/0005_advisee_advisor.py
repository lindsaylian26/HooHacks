# Generated by Django 5.0.3 on 2024-03-24 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisees', '0004_alter_advisee_subject_needed'),
        ('advisors', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisee',
            name='advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advisors.advisor'),
        ),
    ]
