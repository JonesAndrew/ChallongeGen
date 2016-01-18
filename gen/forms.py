from django import forms

class BracketForm(forms.Form):
    bracket_url = forms.CharField(label='Bracket Url', max_length=100)
