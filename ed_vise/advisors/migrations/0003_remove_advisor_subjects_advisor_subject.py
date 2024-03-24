# Generated by Django 5.0.3 on 2024-03-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0002_subjectarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='subjects',
        ),
        migrations.AddField(
            model_name='advisor',
            name='subject',
            field=models.ManyToManyField(related_name='advisors', to='advisors.subject'),
        ),
    ]
