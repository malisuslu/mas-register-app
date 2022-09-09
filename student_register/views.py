from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.views import View

# Create your views here.

# def student_add_update(request, id=0):
#     if request.method == "POST":
#         if id == 0:
#             form = StudentForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Registration Successfull ✓✓")
#                 form = StudentForm()
#             else:
#                 messages.error(request, "Registration failed!!")
#                 form = StudentForm(request.POST)
#         else:
#             student = Student.objects.get(pk=id)
#             form = StudentForm(request.POST, instance=student)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Updated Successfully ✓✓")
#                 form = StudentForm()
#             else:
#                 messages.error(request, "Update failed!!")
#                 form = StudentForm(request.POST)

#     else:
#         if id==0:
#             form = StudentForm()
#         else:
#             student = Student.objects.get(pk=id)
#             form = StudentForm(instance=student)

#     context = {
#         "form" : form
#     }
#     return render(request, 'student_register/student_form.html', context)



#######   Class View Method   ##########
class student_add_update(View):
    def get(self, request, id=0):
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student, form_title="Student Update", button_text="Update")
        return render(request, 'student_register/student_form.html', {"form": form})

    def post(self, request, id=0):
        if id == 0:
            form = StudentForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Registaration Successfull ✓✓")
                form = StudentForm()
            else:
                messages.error(request, "Registaration failed!!")
                form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student, form_title="Student Update", button_text="Update")

            if form.is_valid():
                form.save()
                messages.success(request, "Updated Successfully ✓✓")
                form = StudentForm(form_title="Student Update", button_text="Update")
            else:
                messages.error(request, "Update failed!!")
                form = StudentForm(request.POST, instance=student, form_title="Student Update", button_text="Update")

        return render(request, 'student_register/student_form.html', {"form": form})


def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'student_register/student_list.html', {"student_list": student_list})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list')
