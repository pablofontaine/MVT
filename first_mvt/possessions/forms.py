from django import forms

class PossessionForm(forms.Form):
    item = forms.CharField(
        max_length=40,
        label='Ingrese Item',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese item',
                'required': True,
            }
        ),
    )
    value = forms.IntegerField(
        label='Ingrese valor',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'required': True,
            }
        ),
    )
    owner = forms.CharField(
        max_length=40,
        label='Ingrese dueño/a',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese dueño/a',
                'required': True,
            }
        ),
    )
