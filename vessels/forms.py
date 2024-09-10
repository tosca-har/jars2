from django import forms
from .models import Vessel



mineral_choices = (
    (-1, "Unknown"),
    (6, "Very Dominant"),
    (5, "Major"),
    (4, "Frequent"),
    (3, "Common"),
    (2, "Few"),
    (1, "Minor"),
    (0, "None"),
)

class SearchForm(forms.Form):
    primary_technique = forms.TypedChoiceField(choices= mineral_choices, coerce = int)
    maker_gender = forms.TypedChoiceField(choices= mineral_choices, coerce = int)