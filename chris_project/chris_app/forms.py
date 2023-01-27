from django import forms

from django.forms import NumberInput


FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('mexican', 'Mexican'),
    ('asian', 'Asian'),
]


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField(label="Enter your email address")
    reservation_date = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}))
    # favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH)
    favorite_dish = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_DISH)
