from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones":query}
    return render(request, "Clase/index.html", context)

def agregarCurso(request):
    if request.method == "POST":
        form = forms.AgregarCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:home")
    else:
        form = forms.AgregarCursoForm()
    return render(request, "Clase/agregarCurso.html",context={"form":form})

def agregarEstudiante(request):
    if request.method == "POST":
        form = forms.AgregarEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:home")
    else:
        form = forms.AgregarCursoForm()
    return render(request, "Clase/agregarEstudiante.html",context={"form":form})

def agregarProfesor(request):
    if request.method == "POST":
        form = forms.AgregarProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:home")
    else:
        form = forms.AgregarCursoForm()
    return render(request, "Clase/agregarProfesor.html",context={"form":form})

def agregarComision(request):
    return
