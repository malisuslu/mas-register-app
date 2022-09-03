from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.


def student_add_update(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registration Successfull ✓✓")
                form = StudentForm()
            else:
                messages.error(request, "Registration failed!!")
                form = StudentForm(request.POST)    
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                messages.success(request, "Updated Successfully ✓✓")
                form = StudentForm()
            else:
                messages.error(request, "Update failed!!")
                form = StudentForm(request.POST)

    else:
        if id==0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)

    context = {
        "form" : form
    }
    return render(request, 'student_register/student_form.html', context)



def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'student_register/student_list.html', {"student_list" : student_list})

def verify_delete(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'student_register/verify_delete.html', {"student": student})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list')



