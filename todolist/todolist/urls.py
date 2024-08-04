from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'), # captures aunique integer and passes it to the view as pk. so it knows 
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
]
