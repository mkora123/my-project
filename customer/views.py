from django.shortcuts import render, redirect

from customer.forms import CustomerForm, AppointmentForm
from customer.models import Customer


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    data = Customer.objects.all()
    context = {'data': data}
    return render(request, 'about.html',context)


def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
          form = CustomerForm()

    return render(request, 'contact.html',{'form':form})


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment')
        else:
            form = AppointmentForm()
    return render(request, 'appointment.html', {'form':AppointmentForm()})



def login(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomerForm()
    return render(request, 'login.html', {'form':CustomerForm()})