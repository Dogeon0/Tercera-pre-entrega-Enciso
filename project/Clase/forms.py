from django import forms
from . import models
#class AgregarCursoForm(forms.Form):
#    nombre = forms.CharField()

class AgregarCursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"