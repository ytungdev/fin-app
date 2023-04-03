from django import forms

class AccountForm(forms.Form):
    location = forms.CharField(label='Location', max_length=5)
    provider = forms.CharField(label='Provider', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    curr = forms.CharField(label='Currency', max_length=5)
    remark = forms.CharField(label='Remark', max_length=200, required=False)