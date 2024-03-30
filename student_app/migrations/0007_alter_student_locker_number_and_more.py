# Generated by Django 5.0.3 on 2024-03-30 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_alter_student_locker_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=110, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]
