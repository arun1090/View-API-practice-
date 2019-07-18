from django.db import models

class Employee(models.Model):
    Emp_id = models.IntegerField(primary_key=True,unique=True)
    Firstname=models.CharField(max_length=25)
    Lastname=models.CharField(max_length=25)
    Dateofbirth=models.DateField(verbose_name='DOB')
    Dateofdeath=models.DateField(null=True,blank=True,verbose_name='DOD')
    Summery=models.TextField(max_length=500,default='Please enter the summery details of Employee')
    deathindicator=models.BooleanField()
# Create your models here.
