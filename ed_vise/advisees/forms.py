from django import forms
from .models import Advisee

class AdviseeForm(forms.ModelForm):
    class Meta:
        model = Advisee
        fields = ['subject_needed', 'availability']
