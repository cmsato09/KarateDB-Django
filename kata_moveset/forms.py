from django import forms
from .models import Technique, Stance

class TechniqueCreateForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = [
            'technique_name', 
            'technique_type', 
            'description', 
            'hiragana', 
            'kanji'
        ]