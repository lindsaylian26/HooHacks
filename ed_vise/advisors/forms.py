from django import forms
from .models import Advisor, SubjectArea

class AdvisorForm(forms.ModelForm):
    advising_styles = forms.MultipleChoiceField(
        choices=[('in-person', 'In-person'), ('virtual', 'Virtual'), ('either', 'Either')],
        widget=forms.CheckboxSelectMultiple,
        help_text='Select your advising styles.'
    )
    expertise_areas = forms.ModelMultipleChoiceField(
        queryset=SubjectArea.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text='Select your areas of expertise.'
    )
    available_times = forms.MultipleChoiceField(
        choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')],
        widget=forms.CheckboxSelectMultiple,
        help_text='Select your available times for advising.'
    )
    priority_preference = forms.ChoiceField(
        choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
        help_text='Select the priority level of advisees you prefer.'
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Feedback on advising sessions or system'}),
        required=False
    )

    # Add a name field with initial value and disabled attribute
    name = forms.CharField(
        #disabled=True,  # Set the field as disabled
        required=False,  # Not required as it will be set from the view
        widget=forms.TextInput(attrs={})  # Set the field as readonly
    )


    class Meta:
        model = Advisor
        fields = ['name', 'advising_styles', 'expertise_areas', 'available_times', 'priority_preference', 'feedback']

    def clean_expertise_areas(self):
        expertise_areas = self.cleaned_data.get('expertise_areas')
        if not expertise_areas:
            raise forms.ValidationError('Please select at least one area of expertise.')
        return expertise_areas

    def save(self, commit=True):
        advisor = super().save(commit=False)
        if commit:
            advisor.save()
            self.save_m2m()  # Necessary for saving many-to-many fields
        return advisor
