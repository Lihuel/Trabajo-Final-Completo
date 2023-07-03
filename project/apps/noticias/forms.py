from django import forms
from . import models

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = models.Noticias
        fields = '__all__'