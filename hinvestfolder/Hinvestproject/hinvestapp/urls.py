from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('insert', views.insertdata, name='insertdata'),
    path('update/<id>', views.update, name='updatedata'),
    path('delete/<id>', views.delete, name='deletedata')
]