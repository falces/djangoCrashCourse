from django import forms


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