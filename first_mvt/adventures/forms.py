from django import forms
# from ckeditor.widgets import CKEditorWidget
from adventures.models import Adventure

class AdventuresForm(forms.Form):
    place = forms.CharField(
        max_length=40,
        label='Lugar:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese lugar',
                'required': "True",
            }
        ),
    )
    date = forms.CharField(
        label="Fecha",
        required=False,
        widget=forms.TextInput(
            attrs={
                'required': "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripción: ",
        required=False,
        widget=forms.TextInput(
            attrs={
                "required": "True",
                'placeholder': 'Detalles de la aventura',
            }
        ),
    )

    class Meta:
        model = Adventure
        fields = ['place', 'date', 'description']