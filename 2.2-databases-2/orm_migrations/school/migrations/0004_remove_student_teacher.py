# Generated by Django 4.1.5 on 2023-02-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_teachers_students_student_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
