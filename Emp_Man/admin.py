from django.contrib import admin
from .models import Department_Model,Employee_Model,Employee_Salary_Model
# Register your models here.

admin.site.register(Department_Model)

admin.site.register(Employee_Model)

admin.site.register(Employee_Salary_Model)
