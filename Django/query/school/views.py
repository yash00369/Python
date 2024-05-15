from django.shortcuts import render
from.models import Student,Teacher
# Create your views here.
def home(request):
    #student_data =Student.objects.all()
    #student_data =Student.objects.filter(marks=80)
    #student_data =Student.objects.order_by('marks')
    #student_data =Student.objects.order_by('id').reverse()
    #student_data =Student.objects.values('marks','name')
   
#####second table   Teacher #################
#  qs1 = Student.objects.values_list('id','name',named=True)
#  qs2 = Teacher.objects.values_list('id','name',named=True)
#  student_data=qs1.union(qs2)


#  qs1 = Student.objects.values_list('id','name',named=True)
#  qs2 = Teacher.objects.values_list('id','name',named=True)
#  student_data=qs1.intersection(qs2)
   

 qs1 = Student.objects.values_list('id','name',named=True)
 qs2 = Teacher.objects.values_list('id','name',named=True)
 student_data=qs1.difference(qs2)  
   
 return render(request,'school/home.html',{'students':student_data})
