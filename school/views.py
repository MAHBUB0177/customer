# from django.http.request import UploadHandlerList
from django.shortcuts import render

# Create your views here.
from.models import Student,Teacher
from.models import employee

def index(request):
  

    # employee_data=employee.objects.order_by('name')
   

    # employee_data=employee.objects.get(id=3)
    # employee_data=employee.objects.first()//rerurn table 1st data
    # employee_data=employee.objects.latest('age')//latest ta nibe
    # employee_data=employee.objects.earliest('age')//sobr ager ta nibe

    # employee_data=employee.objects.get(name='jahid')//akoi nme akadhik thkle multiple case error dibe
  
    employee_data=employee.objects.all()
    # one_data=employee.objects.get(pk=1)
    
    # print(employee_data.filter(pk=one_data.pk).exists())//exist match kore thkle true dei
    # employee_data=employee.objects.create(name='diman',age='56',emp_id='12',address='dhaka',salary='8900',join_date='2020-4-4')//table a akta object new create
    # employee_data,created=employee.objects.get_or_create(name='maruf',age='56',emp_id='90',address='dhaka',salary='8900',join_date='2020-4-4')//if value thke then get korbe and data er vitor jbe ar jdi na 
    # thke then create korbe abd created er vitor jbe
    # employee_data=employee.objects.order_by('id').first()
    
    # employee_data=employee.objects.filter(age='25').update(name='mukul')
    # employee_data,created=employee.objects.update_or_create(id=6,name='ok',defaults={'name':'robi'})
    # employee_data,created=employee.objects.update_or_create(id=9,name='karim',age='24',emp_id='55',address='mymunshing',salary=4500,join_date=2020-4-4,defaults={'name':'roni'})
    # man=[
    #     employee(name='kala',age=34,emp_id='677',address='dhanmondi',salary=34000,join_date=2020-2-4),
    #     employee(name='shifa',age=19,emp_id=998,address='dhamnodi',salary=34000,join_date=2020-5-5),
        
    # ]
    # employee_data=employee.objects.bulk_create(man) # //create hbe obj

    # all_employee_data=employee.objects.all()
    # for emp in all_employee_data:
    #     emp.address="rajshahi"
    # employee_data=employee.objects.bulk_update(all_employee_data,['address'])

    employee_data=employee.objects.in_bulk([1,2])
    

  

    print("return:",employee_data)
    
    return render(request, 'school/index.html',{'employees':employee_data})
    

def home(request):

    ####method that return new queryset:

    # student_data=Student.objects.all()
    # student_data=Student.objects.filter(marks=70)//return a query set
    # student_data=Student.objects.exclude(marks=70)//70 bde sob dibe

    # student_data=Student.objects.order_by('?')//randomly changed

    # student_data=Student.objects.order_by('id')
    # student_data=Student.objects.values()//return all value
    # student_data=Student.objects.values('name','roll')//dict akare
    # student_data=Student.objects.values_list('name','roll','marks',named=True)//touple 

    # student_data=Student.objects.dates('pass_date','year')
    # student_data=Student.objects.dates('pass_date','day')
    # student_data=Student.objects.none()//none return 


    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs2.union(qs1)//only return uninon value


    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs2.union(qs1,all=True)//all value return

    student_data=Student.objects.all()

    print("return",student_data)
    print()
    # print("SQL Query:",student_data)
    return render(request, 'school/school.html',{'student':student_data})


