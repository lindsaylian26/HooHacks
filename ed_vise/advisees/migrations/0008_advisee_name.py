# Generated by Django 5.0.3 on 2024-03-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisees', '0007_advisee_is_advisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisee',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]