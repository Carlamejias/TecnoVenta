from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    producto= Producto.objects.all()

    datos = {
        'Productos': producto
    }

    return render(request, 'core/home.html', datos)

def agregar_producto(request, ):

    datos = {
        'form':ProductoForm()
    }

    return render(request, 'core/form.html', datos)

def contacto(request, ):
    
    if request.method=="POST":
        
        miFormulario=FormularioContacto(request.POST)
        
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            ##send_mail(infForm['nombre'], infForm['rut'], infForm['tel'], infForm['ciudad'], infForm['tipo'],
            ##infForm.get('correo',''),['fabisick@gmail.com'],)
            return render(request,"Gracias por contactarse con nosotr@s en 24 hrs habiles le responderemos.")

    else:

        miFormulario=FormularioContacto()

    return render(request, "core/Contacto.html",{"form":miFormulario})

