# Generated by Django 5.0.3 on 2024-03-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisees', '0006_remove_advisee_advisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisee',
            name='is_advisor',
            field=models.BooleanField(default=False),
        ),
    ]