from django.urls import path
from .views import ListTodoView, DetailTodoView

urlpatterns = [
    path('<int:pk>/', DetailTodoView.as_view(), name='todo-detail'),
    path('', ListTodoView.as_view(), name='todo-list')
]
