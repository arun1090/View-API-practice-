from django.shortcuts import render,redirect
from app1.forms import EmployeeForm,RegForm
from app1.models import Employee
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView, ListView,CreateView, UpdateView, DeleteView
import  datetime
from django.utils import timezone


# Create your views here.

def create_detail_view(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
      #  files = request.FILES
        empform = EmployeeForm(data=data)
        print(data)
        if empform.is_valid():
            empform.save()
            msg="success"
            print('form validated')
         #   empform=EmployeeForm()
            return render(request, "app1/home.html", {"form": empform, "message": msg})
        else:
            msg = empform._errors
    else:
        empform = EmployeeForm()
    return render(request, "app1/home.html", {"form": empform, "message": msg})

def list_Employee_views(request):

    list_emp=Employee.objects.all()

    return render (request,"app1/Emp_list.html", {"list_emp":list_emp})

def Reg_view(request):
    msg=""
    if request.method=="POST":
        data =request.POST
        regform=RegForm(data=data)
        if regform.is_valid():
            regform.save()
            msg="sucessefully registered"
            return render(request, "app1/reg.html", {"regform": regform, "message": msg})
        else:
            reg =reform._errors
    else:
        regform = RegForm()

    return render(request, "app1/reg.html", {"regform": regform, "message": msg})

class class_based_view(View):

    def get(self,request,*args,**kwargs):
        emp=Employee.objects.all()
        return render(request, "app1/Emp_list.html", {'list_emp': emp, 'message': "this is get method"})
      #  empform=EmployeeForm()
       # return render(request,"app1/home.html",{'form':empform,'message':"this is get method"})

    def put(self):
        pass

    def post(self,request,*args,**kwargs):
        data=request.POST
        empform = EmployeeForm(data=data)
        print(data)
        if empform.is_valid():
            print('emp form is good')
            empform.save()
            data = Employee.objects.all()
            return render(request, "app1/Emp_list.html", {'list_emp': data, 'message': "this is post method"})
        else:
            empform._errors
            return HttpResponse('wrong Emp_id:')


    def delete(self):
        pass

def update_emp_view(request,pk):
    msg = ""
    emp = Employee.objects.filter(Emp_id=pk)
    print(emp)
    if emp:
        emp = emp[0]
        empform = EmployeeForm(instance=emp)
        if request.method == "POST":
            new_data = request.POST
            empform = EmployeeForm(instance=emp, data=new_data)
            if empform.is_valid():
                empform.save()
                return redirect("/empBCBV")
    else:
        empform=EmployeeForm()
        msg= 'Employee Not Found'
    return render(request, "app1/home.html", {"form": empform, "message": msg})

########Implementeing Generfic Views###################

class EmpDetailView(DetailView):
    model=Employee
    template_name ="app1/Emp_detaillist.html"
    print(object)
    context_object_name='empDV'
    queryset = Employee.objects.exclude(Dateofbirth__gt=datetime.date(2005, 1, 3))

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.Dateofbirth = datetime.date.today()
        obj.Summery = 'hello I changed summery'
      #  obj.save()
        print('Dateofbirth updated ')
        return obj
  #  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
  #      context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
 #       context['Emp_id'] = Employee.objects.all()
   #     if context['Emp_id'] == 666:
   #         print('yes enterted')
   #         context['summery'] = 'summery of 666 git changed'
   #         print(context['Dateofbirth'])
   #     print(context)
   #     return context
   # fields="__all__"

class EmpListview(ListView):
    model=Employee
    template_name = 'app1/Emp_listview.html'
    paginate_by = 100

class EmpCreateView(CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name = 'app1/Emp_createupdateview.html'
    success_url = '/EmpListView'

class EmpUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'app1/Emp_createupdateview.html'
    success_url = '/EmpListView'

class EmpDeleteView(DeleteView):
    model = Employee














