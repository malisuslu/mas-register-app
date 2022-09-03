from django.urls import path
from .views import student_add_update, student_delete, student_list, verify_delete

urlpatterns = [
    path('', student_add_update, name='form'),
    path('student_list/', student_list, name='list'),
    path('update/<int:id>/', student_add_update, name='update'),
    path('verifydelete/<int:id>/', verify_delete, name='verifydelete'),
    path('delete/<int:id>/', student_delete, name='delete'),
]
