from django.contrib import admin
from django.urls import path
from school import views

app_name = "school"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home),
    path('index/',views.index,name='index'),
    

]

