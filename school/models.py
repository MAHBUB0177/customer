from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=300)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    marks=models.IntegerField()
    pass_date=models.DateField()




class Teacher(models.Model):
    name=models.CharField(max_length=300)
    empnum=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    salary=models.IntegerField()
    join_date=models.DateField()


class employee(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    age=models.IntegerField()
    emp_id=models.CharField(max_length=20,null=False)
    address=models.CharField(max_length=30)
    salary=models.IntegerField()
    join_date=models.DateField()

