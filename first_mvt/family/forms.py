from django import forms

class FamilyMemberForm(forms.Form):
    name = forms.CharField(
        label='Nombre: ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'required': 'True',
            }
        ),
    )
    last_name = forms.CharField(
        label='Apellido: ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellido',
                'required': 'True',
            }
        ),
    )
    age = forms.IntegerField(
        label='Edad: ',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Edad',
                'required': 'True',
            }
        ),
    )
    relationship = forms.CharField(
        label='Relación: ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Relación',
                'required': 'True',
            }
        ),
    )