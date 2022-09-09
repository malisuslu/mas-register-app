from django import forms
from .models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_tailwind.layout import Submit
from crispy_forms.layout import Column, Row, Div, HTML


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # '__all__' if you wanna select all
        fields = ["full_name",
                  "number",
                  "mobile",
                  "email",
                  "gender",
                  "path", ]
        labels = {"full_name": "Full Name",
                  "number": "Student Number",
                  "mobile": "Phone Number",
                  "email": "E-mail",
                  "gender": "Gender",
                  "path": "Learning Path"}

    # crispy helper

    def __init__(self, *args, **kwargs):

        form_title = "Student Register"
        button_text = "Submit"
        if len(kwargs) > 1:
            form_title=kwargs["form_title"]
            button_text=kwargs["button_text"]

        # if "instance" in kwargs:
        #     instance = kwargs["instance"]
        #     id_num = instance.id_num()            
        #     student = Student.objects.get(pk=id_num)
        #     print(student.full_name)

        if "form_title" in kwargs:
            kwargs.pop("form_title")
            kwargs.pop("button_text")
        super().__init__(*args, **kwargs)


        self.helper = FormHelper()

        self.helper.layout = Layout(
            Div(
                Fieldset(
                    form_title,
                    "full_name",
                    "mobile",
                    "email",
                    "gender",
                    Row(Column("number", css_class="w-1/3 pr-2"),
                        Column("path", css_class="w-2/3 pl-2")),
                    # css_class="max-w-3xl px-8 mx-auto"
                ),
                Row(
                    Submit("submit", button_text, css_class="bg-transparent hover:bg-green-600 text-green-700 font-semibold hover:text-white py-2 px-4 mr-2 w-2/3 border border-green-500 hover:border-transparent rounded cursor-pointer"),
                    HTML("""
                    <a class="text-center bg-transparent hover:bg-blue-600 text-blue-700 font-semibold hover:text-white py-2 px-4 w-1/3 ml-2 border border-blue-500 hover:border-transparent rounded cursor-pointer" href="/student_list">Back to list</a>
                    """)
                ),
                css_class=" box-content max-w-xl px-8 mx-auto bg-gray-200 py-10 mt-0 sm:mt-6 border-[16px] border-white"
            ),
        )



