from django import forms

class StockForm(forms.Form):
    market  = forms.CharField(label='Market', max_length=5)
    symbol  = forms.CharField(label='Symbol', max_length=10)
    name    = forms.CharField(label='Name', max_length=10)
    curr    = forms.CharField(label='Curr', max_length=5)