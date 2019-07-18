from django import forms
from app1.models import Employee
from django.contrib.auth.models  import User

print('welcome to Emplyeeform')

class RegForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=250)
    class Meta:
        model=User
        fields=['username','password','email','first_name']

    def clean_password(self):
        password = self.data.get("password")
        c_password = self.data.get("confirm_password")
        if password != c_password:
            err = "passwords not matched"
            raise forms.ValidationError(err)
        return password


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields= "__all__"
        print('welcome to Emplyeeform1')

    def clean_Emp_id(self,value=None):
        empid=self.data.get("Emp_id")

        a = 1995
        if int(empid) == a:
            raise forms.ValidationError("Employee Id should not start with 9 ")
        return empid



