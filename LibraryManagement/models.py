from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class Employee(models.Model):
    empId=models.AutoField(primary_key=True)
    eName=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
    salary=models.IntegerField()

    def __str__(self):
        return self.eName +' | '+self.email + ' | '+str(self.salary)

class Librarian(models.Model):
    LibId=models.AutoField(primary_key=True)
    EnrollmentNO = models.CharField(max_length=10,null=True,unique=True)
    Name=models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    phoneNO = models.CharField(max_length=10,null=True)

    
    def __str__(self):
        return str(self.EnrollmentNO) +' | '+ self.Name + ' | '+ self.branch + '|' + self.phoneNO

class Books(models.Model):
    BookId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.BookId) +' | '+self.Name + ' | '+self.Author

def get_expiry():
    return datetime.today() + timedelta(days=15)
class IssuedBook(models.Model):
    EnrollmentNO=models.CharField(max_length=30)
    BookId=models.CharField(max_length=30,default='0')
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return str(self.EnrollmentNO)
