# forms.py
from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['name', 'date_of_birth', 'salary', 'img']

        labels = {
            'name': 'Full Name',
            'date_of_birth': 'Date of Birth',
            'salary': 'Salary',
            'img': 'Image',
        }

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

