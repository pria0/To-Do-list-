
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('to-do/',views.to_do,name='to_do'),
    path('todo-delete/<int:tid>',views.todo_delete,name='todo_delete'),
]
