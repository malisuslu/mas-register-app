from django.urls import path
from .views import student_add_update, student_delete, student_list

urlpatterns = [
    path('', student_add_update.as_view(), name='form'),
    path('student_list/', student_list, name='list'),
    path('update/<int:id>/', student_add_update.as_view(), name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
]
