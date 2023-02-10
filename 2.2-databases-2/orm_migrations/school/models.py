from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, verbose_name='Класс')
    teachers = models.ManyToManyField(Teacher, through='Teachers_Students', related_name='students')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class Teachers_students(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    class Meta:
        verbose_name = 'Учитель и ученик'
        verbose_name_plural = 'Учителя и ученики'

        def __str__(self):
            return self.name

