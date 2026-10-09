from django import forms
class StudentRegisterationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    roll_number = forms.IntegerField(label='Roll Number')
    department = forms.CharField(label='Department', max_length=100)
    year = forms.IntegerField(label='Year')
    email=forms.EmailField(label='Email')
    mobile_number=forms.CharField(label='Mobile Number', max_length=10)
    age=forms.IntegerField(label='Age',min_value=1,max_value=100)


class EmployeeForm(forms.Form):
    DEPARTMENTS=[("HR","HR"),("IT","IT"),("SALES","SALES"),("ACCOUNTS","ACCOUNTS"),]
    name=forms.CharField(label="Employee Name",max_length=100)
    emp_id=forms.CharField(label="Employee ID",max_length=10)
    department=forms.ChoiceField(label="Department",choices=DEPARTMENTS)
    salary=forms.DecimalField(label="salary",min_value=0)

class CourseForm(forms.Form):
    COURSES=[("python","python"),("java","java"),("django","django"),("Data Science","Data Science"),]
    name=forms.CharField(label="Employee Name",max_length=100)
    email=forms.EmailField(label='Email')
    course=forms.ChoiceField(label="Course Name",choices=COURSES)
    duration=forms.IntegerField(label="Duration(In months)",min_value=1)
