from django.urls import path
from . import views

urlpatterns = [
    path('', views.addContact, name="addcontact"),
    path('update/<int:id>/', views.updateContact, name="updatecontact"),
    path('delete/<int:id>/', views.deleteContact, name="deletecontact")
]
