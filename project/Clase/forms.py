from django import forms
from . import models
#class AgregarCursoForm(forms.Form):
#    nombre = forms.CharField()

class AgregarCursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"

class AgregarEstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = "__all__"    

class AgregarProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"      