from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('proff',views.students, name='proff'),
        path('users',views.teachers, name='users')
]