from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:id>', views.detail_task, name='task_detail'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>', views.update_task, name='update_task'),
]
