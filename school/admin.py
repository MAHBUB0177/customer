from django.contrib import admin

# Register your models here.
from.models import Student
from.models import Teacher
from.models import employee

@admin.register(Student)

class  StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']


@admin.register(Teacher)
class  TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','empnum','city','salary','join_date']

@admin.register(employee)
class  employeeAdmin(admin.ModelAdmin):
    list_display=['id','name','age','emp_id','address','salary','join_date']
