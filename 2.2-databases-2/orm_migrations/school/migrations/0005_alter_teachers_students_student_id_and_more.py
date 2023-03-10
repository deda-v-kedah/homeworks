# Generated by Django 4.1.5 on 2023-02-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers_students',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='teachers_students',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher', verbose_name='Учитель'),
        ),
    ]
