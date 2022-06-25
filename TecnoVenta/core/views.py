from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    producto= Producto.objects.all()

    datos = {
        'Productos': producto
    }

    return render(request, 'core/home.html', datos)

    def form_producto(request):
    
    datos = {
        'form': ProductoForm()

    }
    if request.method== 'POST':
        
        formulario = ProductoForm(request.POST)
        
        if formulario.is_valid:
        
            formulario.save()
        
            datos['mesaje'] = "Guardados correctamente"

    return render(request, 'core/form.html', datos)
