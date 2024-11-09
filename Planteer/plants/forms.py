from django import forms
from .models import Plant, Country

class PlantForm(forms.ModelForm):
    native_to = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'add-plant-dropdown-menu'}),
        label="Native to"
    )

    class Meta:
        model = Plant
        fields = ['title', 'about', 'used_for', 'is_edible', 'native_to', 'image', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-plant-form-control', 'placeholder': 'Enter plant title'}),
            'about': forms.Textarea(attrs={'class': 'add-plant-form-control', 'rows': 4, 'placeholder': 'Write about the plant'}),
            'used_for': forms.Textarea(attrs={'class': 'add-plant-form-control', 'rows': 4, 'placeholder': 'What is the plant used for?'}),
            'is_edible': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'add-plant-radio-group'}),
            'image': forms.ClearableFileInput(attrs={'class': 'add-plant-form-control', 'required': False}),
            'category': forms.Select(attrs={'class': 'add-plant-form-control', 'required': 'required'}),
        }
