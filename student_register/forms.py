from django import forms
from .models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder
from crispy_tailwind.layout import Submit, Button, Reset, Alert
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
        # labels = {"full_name": "Name"}
        # labels = {"mobile": "Mobile"}
        # labels = {"email": "E-mail"}
        # labels = {"number": "Student Number"}
        # labels = {"gender": "Gender"}
        # labels = {"path": "Path"}

    # crispy helper
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    "Student Registration",
                    "full_name",
                    "mobile",
                    "email",
                    "gender",
                    Row(Column("number", css_class="w-1/3 pr-2"),
                        Column("path", css_class="w-2/3 pl-2")),
                    # css_class="max-w-3xl px-8 mx-auto"
                ),
                Row(
                    Submit("submit", "Submit", css_class="bg-transparent hover:bg-green-600 text-green-700 font-semibold hover:text-white py-2 px-4 mr-2 w-2/3 border border-green-500 hover:border-transparent rounded cursor-pointer"),
                    HTML("""
                    <a class="text-center bg-transparent hover:bg-blue-600 text-blue-700 font-semibold hover:text-white py-2 px-4 w-1/3 ml-2 border border-blue-500 hover:border-transparent rounded cursor-pointer" href="/student_list">Back to list</a>
                    """)
                ),
                css_class=" box-content max-w-xl px-8 mx-auto bg-gray-200 py-10 mt-0 sm:mt-6 border-[16px] border-white"
            ),
        )
