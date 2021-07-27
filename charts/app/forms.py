from django.db.models import fields
from django.forms import widgets
from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['class_n','number_of']
        widgets = {
            'class_n':forms.TextInput(attrs={'placeholder':'10','class':'form-control'}),
            'number_of':forms.NumberInput(attrs={'placeholder':'90','class':'form-control'})
        }