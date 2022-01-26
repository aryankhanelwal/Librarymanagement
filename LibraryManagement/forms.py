from django import forms
from .models import *


class EmpRegisForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,min_length=1, max_length=16)
    class Meta:
        model = Employee
        fields ='__all__'

class SigninForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,min_length=1, max_length=16)
    class Meta:
		    model = Employee
		    fields = ['email','password']

class LibRegisForm(forms.ModelForm):
        class Meta:
            model = Librarian
            fields = '__all__'

class BookRegisForm(forms.ModelForm):
        class Meta:
            model = Books
            fields = '__all__'


            
class IssuedBookForm(forms.Form):
    BookId=forms.ModelChoiceField(queryset=Books.objects.all(),empty_label="BookId", to_field_name="BookId",label='BookID')
    EnrollmentNO=forms.ModelChoiceField(queryset=Librarian.objects.all(),empty_label="EnrollmentNO",to_field_name='EnrollmentNO',label='EnrollmentNO')
    




