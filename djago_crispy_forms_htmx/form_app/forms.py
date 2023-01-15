from django import forms
from datetime import datetime

COURSE_CHOICES =(
    (1, 'Law'),
    (2, 'Computer Science'),
    (3, 'Business Administration'),
)
class EnrollmentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.RadioSelect #change widget to radio select
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={  # change widget to date widget
        'type': 'date', 
        'max': datetime.now().date()})) #prevent users from entering a future date