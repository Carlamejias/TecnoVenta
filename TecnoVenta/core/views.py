from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    producto= Producto.objects.all()

    datos = {
        'Productos': producto
    }

    return render(request, 'core/home.html', datos)

    
