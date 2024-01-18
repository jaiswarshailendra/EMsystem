from django.shortcuts import render,redirect
from .models import Department_Model, Employee_Model,Employee_Salary_Model
from django.contrib.auth import authenticate,login,logout
from .forms import Employee_Form,Employee_Salary_Form,Department_Form


def home(request): # Home page
    return render(request, 'html/home.html')
def Department_Reporting(request): # filter data based on designation
    manager = Employee_Model.objects.filter(designation='Manager')  
    return render(request, 'html/reporting.html', { 'managers': manager})

def Singin(request):# Authenticate user 
    if request.user.is_authenticated:
        return render(request,"html/home.html")
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
    return render(request,"html/admin.html")

def Logout_User(request):#Logout user
    logout(request)
    return redirect("/")

def Employee_View(request):#All Employee view
    if request.user.is_authenticated and request.user.is_superuser:
        emp=Employee_Model.objects.all()
        return render(request,'html/emp.html',{'emp':emp})
    else:
        return redirect("/singin")

def Employee_CP(request,id=None):#create and update employee
    if request.user.is_authenticated and request.user.is_superuser:
        if id== None:
            form=Employee_Form()
            if request.method=='POST':
                form=Employee_Form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("/employee")
                return render(request,"html/create.html",{"form":form})
        else:
            dep=Employee_Model.objects.get(id=id)
            form=Employee_Form(request.POST or None,instance=dep)
            if request.method=="POST":
                if form.is_valid():
                    form.save()
                    return redirect("/employee")
            return render(request,"html/create.html",{"form":form})
        return render(request,"html/create.html",{"form":form})
    else:
        return Singin(request)

def Employee_Delete(request,id):# Delete employee
    if request.user.is_superuser and request.user.is_authenticated:
        Employee_Model.objects.get(id=id).delete()
        return redirect("/employee")
    else:
        return redirect('/singin')
    
def Department_View(request):# View all departments
    if request.user.is_authenticated and request.user.is_superuser:
            dept=Department_Model.objects.all()
            return render(request,"html/department.html",{"dept":dept})
    else:
        return redirect("/a")
    
def Department_CP(request,id=None):# create update departments
    if request.user.is_authenticated and request.user.is_superuser:
        if id == None:
            form = Department_Form()
            if request.method=="POST":
                form=Department_Form(request.POST)
                if form.is_valid():
                    dep=form.save()
                    return redirect("/department")
            return render(request,"html/dept.html",{"form":form})
        else:
            dep=Department_Model.objects.get(id=id)
            form=Department_Form(request.POST or None,instance=dep)
            if request.method=="POST":
                if form.is_valid():
                    form.save()
                    return redirect("/department")
            return render(request,"html/dept.html",{"form":form})
    else:
        return redirect("/a")
    
def Department_Delete(request,id):# delete department
    if request.user.is_superuser:
        dp=Department_Model.objects.get(id=id).delete()
        return redirect('/department')
    else:
        return redirect("/singin")

def Employee_Salary_View(request,sd=None,ed=None):# view salary of all employee 
    if request.user.is_authenticated and request.user.is_superuser:
        if request.POST.get("sd")==None or request.POST.get("ed")==None:
            emps=Employee_Salary_Model.objects.all()
            return render(request,'html/salary.html',{'emps':emps})
        else:
            sd=request.POST.get("sd")
            ed=request.POST.get("ed")
            try:
                emps=Employee_Salary_Model.objects.filter(start_date=sd,end_date=ed)
            except:
                return redirect("/salary")
            return render(request,'html/salary.html',{'emps':emps})
    else:
        return redirect("/singin")
    
def Employee_Salary_CP(request,id=None):# create update employees salary
    if request.user.is_authenticated and request.user.is_superuser:
        if id==None:
            emp=Employee_Model.objects.all()
            form=Employee_Salary_Form()
            if request.method=="POST":
                print(2)
                form=Employee_Salary_Form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("/salary")
            return render(request,"html/sup.html",{"form":form,"emp":emp})
        else:
            emp=Employee_Salary_Model.objects.get(id=id)
            form=Employee_Salary_Form(request.POST or None,instance=emp)
            if request.method=="POST":
                if form.is_valid():
                    form.save()
                    return redirect('/salary')
            return render(request,"html/sup1.html",{"form":form,"emp":emp})
    else:
        return redirect("/singin")

def sdelete(request,id): # delete any employee with their salary
    if request.user.is_superuser and request.user.is_authenticated:
        Employee_Salary_Model.objects.get(id=id).delete()
        return redirect("/salary")
    else:
        return redirect("/singin")