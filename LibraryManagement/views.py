from django.shortcuts import render,redirect
from .models import *
from .forms import *
from datetime import datetime,timedelta,date


def firstpage(request):
    return render(request,'firstpage.html')

def Librarians(request):
    return render(request,'Librarian1.html')
    
def aboutus(request):
    return render(request,'aboutus.html')



def ShowData(request):
    data = Employee.objects.all()
    return render(request, 'Datashow.html', {'mydata': data})

def librariansshow(request):
     students=Librarian.objects.all()
     return render(request,'librariansshow.html',{'studentshow':students})

def StudentRegis(request):
    if request.method == "GET":
        form=LibRegisForm()
    if request.method == "POST":
        form = LibRegisForm(request.POST)
        form.save()
        return redirect('Librarians')
   
    return render(request,'studentadd.html',{'StudentForm':form})


def empRegis(request):
    if request.method == "GET":
        form=EmpRegisForm()
    if request.method == "POST":
        form = EmpRegisForm(request.POST)
        form.save()
        return redirect('login')
   
    return render(request,'empRegistration.html',{'empForm':form})
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        
        q = Employee.objects.filter( 
                    email=  request.POST['email'],
                    password = request.POST['password'] )
        if len(q)>0:
                    return redirect('Librarians')
        else:
                   return redirect('login')
    else:
        form = SigninForm()
        return render( request, 'login.html', {'form':form} )

def LibRegis(request):
    if request.method == "GET":
        form=LibRegisForm()
    if request.method == "POST":
        form = LibRegisForm(request.POST)
        form.save()
        return redirect('Librarian')
   
    return render(request,'empRegistration.html',{'empForm': form1})



def BookRegis(request):
    if request.method == "GET":
        form2=BookRegisForm()
    if request.method == "POST":
        form2 = BookRegisForm(request.POST)
        form2.save()
        return redirect('BookData')

    return render(request,'BookRegistration.html',{'BookForm': form2})


def BookData(request):
    data1 = Books.objects.all()
    return render(request, 'Bookshow.html', {'Bookdata': data1})

def LibrarianData(request):
    data1 = Books.objects.all()
    return render(request, 'Bookshow.html', {'Bookdata': data1})


def Book_delete(request):
    BookId = request.GET['BookId']
    Books.objects.filter(BookId = BookId).delete();
    return redirect('BookData')


def issuebook(request):
    form=IssuedBookForm()
    if request.method=='POST':
        
        form=IssuedBookForm(request.POST)
        if form.is_valid():
            obj=IssuedBook()
            obj.EnrollmentNO=request.POST.get('EnrollmentNO')
            obj.BookId=request.POST.get('BookId')
            obj.save()
            return render(request,'issuebook.html')
    return render(request,'issuebook.html',{'form':form})

def viewissuedbook(request):
    issuedbooks=IssuedBook.objects.all()
    li=[]
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10


        books=list(Books.objects.filter(BookId=ib.BookId))
        students=list(Librarian.objects.filter(EnrollmentNO=ib.EnrollmentNO))
        i=0
        for l in books:
            t=(students[i].Name,students[i].EnrollmentNO,books[i].Name,books[i].Author,issdate,expdate,fine)
            i=i+1
            li.append(t)

    return render(request,'viewissued.html',{'li':li})


def Issuedelete(request):
    EnrollmentNO = request.GET['EnrollmentNO']
    IssuedBook.objects.filter(EnrollmentNO=  EnrollmentNO).delete();
    return redirect('viewissueddbook')