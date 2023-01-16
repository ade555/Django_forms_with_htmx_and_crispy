from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

COURSE_CHOICES =(
    (1, 'Law'),
    (2, 'Computer Science'),
    (3, 'Business Administration'),
)
class EnrollmentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('form')
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'hx-trigger': 'keyup',
                'hx-get': reverse_lazy('form')
            }
        )
    )
    age = forms.IntegerField()
    course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.RadioSelect #change widget to radio select
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={  # change widget to date widget
        'type': 'date', 
        'max': datetime.now().date()})) #prevent users from entering a future date