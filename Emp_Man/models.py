from django.db import models

# Create your models here.

class Department_Model(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Employee_Model(models.Model):
    Designation_Choices = [
        ('Associate', 'Associate'),
        ('TL', 'Team Leader'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    designation = models.CharField(max_length=20, choices=Designation_Choices)
    reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department_Model, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee_Salary_Model(models.Model):
    employee = models.ForeignKey(Employee_Model, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} {self.salary} {self.start_date} {self.end_date}"

