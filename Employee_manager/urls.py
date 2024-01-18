"""
URL configuration for Employee_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Emp_Man import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('eh', views.Department_Reporting),
    path("singin",views.Singin),
    path("logout",views.Logout_User),
    path("employee/",views.Employee_View),
    path("emp/",views.Employee_CP),
    path("emp/<int:id>",views.Employee_CP),
    path("edelete/<int:id>",views.Employee_Delete),
    path("department",views.Department_View),
    path("dept/",views.Department_CP),
    path("dept/<int:id>",views.Department_CP),
    path("ddelete/<int:id>",views.Department_Delete),
    path("salary",views.Employee_Salary_View),
    path("sup",views.Employee_Salary_CP),
    path("sup/<int:id>",views.Employee_Salary_CP),
    path("sdelete/<int:id>",views.sdelete)

    #path('department_salary_costs/', views.department_salary_costs, name='department_salary_costs'),
]

