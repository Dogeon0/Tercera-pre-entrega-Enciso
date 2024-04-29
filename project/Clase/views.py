from django.shortcuts import render
from . import models, forms

# Create your views here.


def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones":query}
    return render(request, "Clase/index.html", context)

def agregarCurso(request):
    if request.method == "POST":
        print("POSTEADOOOOOO")
    else:
        form = forms.AgregarCursoForm()
    return render(request, "Clase/agregarCurso.html",context={"form":form})

def agregarEstudiante(request):
    return

def agregarProfesor(request):
    return

def agregarComision(request):
    return
