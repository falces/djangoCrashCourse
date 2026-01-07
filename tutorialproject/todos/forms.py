from django import forms
from .models import Todos


class PersonForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Nombre',
    )
    age = forms.IntegerField(
        label='Edad',
    )
    job = forms.CharField(
        max_length=100,
        required=False,
        label='Trabajo',
    )
    
class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todos
        fields = ['title', 'description', 'done', 'deadline', 'priority']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
