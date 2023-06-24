from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.


def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(f"insert new emplyee {form}")
        if form.is_valid():
            try:
                form.save()
                return redirect('dt-show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'myDatable/add.html', {'form': form})


def index(request):
    employees = Employee.objects.all().order_by('-id')
    form = EmployeeForm()
    return render(request, "myDatable/show.html", {'employees': employees,  'form': form})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'myDatable/edit.html', {'employee': employee})


def update(request, id):
    
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)

    print(f"update emplyee {form}")
    if form.is_valid():
        form.save()
        return redirect('dt-show')
    return render(request, 'myDatable/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('dt-show')
