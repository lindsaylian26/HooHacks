# Generated by Django 5.0.3 on 2024-03-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0006_advisor_is_advisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
