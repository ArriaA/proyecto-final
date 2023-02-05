"""blog URL Configuration, name =


"""
from django.contrib import admin
from django.urls import path
from articulos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('comentario/', views.comentario, name = 'comentario'),
    path('tasks/', views.tasks, name = 'tasks') ,
    path('crearcuenta/', views.crearcuenta, name = 'crearcuenta'),
    path('iniciarsesion/', views.iniciarsesion, name = 'iniciarsesion'),
    path('cerrarsesion/', views.cerrarsesion, name = 'cerrarsesion'),
]
