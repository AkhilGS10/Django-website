# Generated by Django 5.1.4 on 2025-02-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_date_of_birth_student_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hobbies',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
