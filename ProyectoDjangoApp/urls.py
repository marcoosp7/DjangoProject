from django.urls import path

from ProyectoDjangoApp import views

urlpatterns = [
    #quito el admin 
    path('',views.home, name="Home"),   #esta no lleva nada dentro del path
    path('servicios',views.servicios, name="Servicios"),
    path('tienda',views.tienda, name="Tienda"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"),
]