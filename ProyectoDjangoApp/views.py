from django.shortcuts import render,HttpResponse

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