from django.shortcuts import render
#1.
# def profile(request):
#     return render(request, 'firstapp/first.html')
#2.
# def gallery(request):
#     return render(request, 'firstapp/gallery.html')
#3.
# def marks_calculator(request):
#     return render(request, 'firstapp/calculator.html')
#4.
# def quiz(request):
#     return render(request, 'firstapp/quiz.html')
#5.
# def department(request):
#     return render(request, 'firstapp/department.html')
#6.
# def clgDept(request):
#     return render(request, 'firstapp/clgDept.html')

# from django.shortcuts import render
# from .forms import StudentRegisterationForm

# def studentForm(request):
#     if request.method == 'POST':
#         form = StudentRegisterationForm(request.POST)

#         if form.is_valid():
#             return render(
#                 request,
#                 'firstapp/student_result.html',
#                 {'data': form.cleaned_data}
#             )
#     else:
#         form = StudentRegisterationForm()

#     return render(
#         request,
#         'firstapp/student_register.html',
#         {'form': form}
#     )

# from .forms import EmployeeForm
# def employee_register(request):
#     if request.method=="POST":
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             return render(request,"firstapp/employee_details.html",{"data":form.cleaned_data})
#     else:
#         form=EmployeeForm()  
#     return render(request,"firstapp/employee_form.html",{"form":form})

from .forms import CourseForm
def course_register(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            return render(request,"firstapp/course_details.html",{"data":form.cleaned_data})
    else:
        form=CourseForm()  
    return render(request,"firstapp/course_form.html",{"form":form})