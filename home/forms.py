from django import forms 
from.models import mytodo

class TodoForm(forms.ModelForm):
    
    class Meta:    
        model = mytodo
        fields = ['task',]
        