from django import forms

COURSE_CHOICES =(
    (1, 'Law'),
    (2, 'Computer Science'),
    (3, 'Business Administration'),
)
class EnrollmentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    dob = forms.DateField()