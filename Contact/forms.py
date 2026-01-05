from django import forms

class FormApp (forms.Form):
    name = forms.CharField (label='', max_length=100, required=True, widget=forms.TextInput (attrs={'placeholder': 'Name ...', 'id': 'name'}))
    email = forms.EmailField (label='', max_length=50, required=True, widget=forms.EmailInput (attrs={'placeholder': 'email ...', 'id':'email'}))
    phone = forms.IntegerField (label='', widget=forms.NumberInput ({'placeholder': 'phone ...', 'id':'phone'}))
    commentary = forms.CharField (label='', required=True, widget=forms.Textarea (attrs={'placeholder': 'commentary ...', 'id': 'comentary'}))