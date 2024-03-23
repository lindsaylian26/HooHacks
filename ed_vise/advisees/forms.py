from django import forms
from .models import Advisee, SubjectArea
from advisors.models import Advisor

class AdviseeForm(forms.ModelForm):
    preferred_advisor = forms.ModelChoiceField(
        queryset=Advisor.objects.all(),
        required=False,
        help_text='Select your preferred advisor if any.'
    )
    subject = forms.ModelChoiceField(
        queryset=SubjectArea.objects.all(),
        required=True,
        help_text='Select your subject area.'
    )
    preferred_advising_style = forms.ChoiceField(
        choices=[('in-person', 'In-person'), ('virtual', 'Virtual'), ('either', 'Either')],
        help_text='Select your preferred advising style.'
    )
    meeting_times = forms.MultipleChoiceField(
        choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')],
        widget=forms.CheckboxSelectMultiple,
        help_text='Select your preferred meeting times.'
    )
    urgency = forms.ChoiceField(
        choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
        help_text='Select the urgency of your advising need.'
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Any previous advising experience feedback?'}),
        required=False
    )

    class Meta:
        model = Advisee
        fields = ['availability', 'preferred_advisor', 'subject',
                  'preferred_advising_style', 'meeting_times', 'urgency', 'feedback']

    def clean_interests(self):
        interests = self.cleaned_data.get('interests')
        if not interests:
            raise forms.ValidationError('Please select at least one area of interest.')
        return interests

    def save(self, commit=True):
        advisee = super().save(commit=False)
        if commit:
            advisee.save()
            self.save_m2m()  # Needed to save many-to-many relationships
        return advisee
