from django.shortcuts import render,HttpResponse, redirect
from django.core.mail import send_mail
from .models import Mensaje
from django.http import HttpResponseRedirect


#creo tantas vistas como paginas

def home(request):

    return render(request, "ProyectoDjangoApp/home.html")  #devuelve esto (url)

def servicios(request):
    return render(request, "ProyectoDjangoApp/servicios.html") #devuelve esto

def tienda(request):
    return render(request, "ProyectoDjangoApp/tienda.html")  #devuelve esto

def blog(request):
    return render(request, "ProyectoDjangoApp/blog.html")  #devuelve esto

def contacto(request):
    return render(request, "ProyectoDjangoApp/contacto.html")  #devuelve esto

from django.shortcuts import render, redirect
from .models import Mensaje

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        nuevo_mensaje = Mensaje(nombre=nombre, email=email, mensaje=mensaje)
        nuevo_mensaje.save()
        return redirect('Contacto')  
    return render(request, 'ProyectoDjangoApp/contacto.html')

    return HttpResponse("Mensaje enviado correctamente")