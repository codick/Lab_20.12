from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('add/', views.add),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
]