from django import forms
from ghost.models import ModelForBoastsAndRoasts
from django.utils import timezone


class FormForBoastsAndRoasts(forms.Form):
    body = forms.CharField(max_length=280)
    ROAST_OR_BOAST = ((True, 'Boast'), (False, 'Roast'))
    boast = forms.ChoiceField(choices=ROAST_OR_BOAST)
