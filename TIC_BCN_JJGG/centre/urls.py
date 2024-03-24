from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('teachers',views.teachers, name='teachers'),
        path('students',views.students, name='users'),
        path('teachers/teacher/<int:pk>/', views.teacher, name='teacher'),
        path('students/student/<int:pk>/', views.student, name='user'),
        path('user-form/',views.user_form,name='user_form')
]