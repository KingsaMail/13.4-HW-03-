from django import forms

class TestForm(forms.Form):
    number_1 = forms.IntegerField()
    number_2 = forms.IntegerField()