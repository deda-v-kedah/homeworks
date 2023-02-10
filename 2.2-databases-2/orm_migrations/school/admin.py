from django.contrib import admin

from .models import Student, Teacher, Teachers_students


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Teachers_students)
class Teachers_StudentsAdmin(admin.ModelAdmin):
    
    list_display= ['teacher_id', 'student_id']


