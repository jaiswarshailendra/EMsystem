# EMsystem
This application is built using Django, In this application we can add, remove, filter employees , department and employee's salary

## How to use 
Clone the project
```
  git clone https://github.com/jaiswarshailendra/EMsystem.git
```

Install dependencies
```
  pip install -r requirements.txt
```

Start the server
```
  python manage.py runserver for windows
  python3 manage.py runserver for linux
```
## To access employee detail, department, employes's salary
Login as admin
`
Username :- admin,
password :- qwerty
`
## urls
    path('',views.home),    To access Home Page
    
    path('eh', views.Department_Reporting),   To get Employee Hierarchy means who is reporting to whom
    
    path("singin",views.Singin),    User login page
    
    path("logout",views.Logout_User),   logout user 
    
    path("employee/",views.Employee_View),    To get all employee detail
    
    path("emp/",views.Employee_CP),     To create an employee, only if the user is an administrator. 
    
    path("emp/<int:id>",views.Employee_CP),    To update an employee, only if the user is an administrator and uses employee_id
    
    path("edelete/<int:id>",views.Employee_Delete),    To delete an employee, only if the user is an administrator. 
    
    path("department",views.Department_View),      To get all departments details
        
    path("dept/",views.Department_CP),   To create a department, only if the user is an admin
    
    path("dept/<int:id>",views.Department_CP),    To update an department, by thier department_id
    
    path("ddelete/<int:id>",views.Department_Delete),    To delete any department
    
    path("salary",views.Employee_Salary_View),    To get all employees salary as per month
    
    path("sup",views.Employee_Salary_CP),  To create employee with thier salary
    
    path("sup/<int:id>",views.Employee_Salary_CP),  To update employees salary details 
    
    path("sdelete/<int:id>",views.sdelete)    to delete employee salary detail
