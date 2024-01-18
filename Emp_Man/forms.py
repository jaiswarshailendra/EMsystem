from .models import Employee_Model,Employee_Salary_Model,Department_Model
from django import forms
class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee_Model
        fields='__all__'

class Department_Form(forms.ModelForm):
    class Meta:
        model=Department_Model
        fields="__all__"

class Employee_Salary_Form(forms.ModelForm):
    class Meta:
        model=Employee_Salary_Model
        fields="__all__"