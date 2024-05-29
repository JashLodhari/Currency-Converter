from datetime import datetime
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import Contact
from home.models import pdf
from django.shortcuts import render
from home.models import book
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #pdf_files=pdf.objects.all()
    #return render(request,'base.html',locals())
    context={'pdf_file':pdf.objects.all()}
    return render(request,'base.html',context)

def studentcorner(request):
    context={'pdf_file':pdf.objects.all()}
    return render(request,'sc.html',context)
    
def library(request):
    context={'books':book.objects.all()}
    Books = book.objects.all()
    paginator = Paginator(Books, 25) # Show 25 books per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'library.html',{'context':context,'page_obj': page_obj})
    #books=book.objects.all()
    #return render(request, 'library.html',locals())

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venue = book.objects.filter(Book_name__contains = searched)
        return render(request,'library.html',{'searched':searched,'venue':venue})
    else:
        return render(request,'library.html')

def unitconverter(request):
    return render(request, 'uc.html')

def contact(request):
     if request.method == "POST":
          fname  = request.POST.get('fname')
          lname = request.POST.get('lname')
          email  = request.POST.get('email')
          subject  = request.POST.get('subject')
          contact = Contact(fname=fname, lname=lname, email=email, subject=subject, date=datetime.today())
          contact.save()
          messages.success(request, 'Your message has been sent succesfully!')
     return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def length(request):
    return render(request, 'length.html')
    
def speed(request):
    return render(request, 'speed.html')

def temperature(request):
    return render(request, 'temperature.html')

def weight(request):
    return render(request, 'weight.html')

def area(request):
    return render(request, 'area.html')

def time(request):
    return render(request, 'time.html')

def discount(request):
    return render(request, 'discount.html')

def data(request):
    return render(request, 'data.html')

def mass(request):
    return render(request, 'mass.html')

def age(request):
    return render(request, 'age.html')

def bmi(request):
    return render(request, 'bmi.html')

def pressure(request):
    return render(request, 'pressure.html')

def currencyconverter(request):
    return render(request, 'money.html')