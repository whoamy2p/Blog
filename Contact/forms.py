from django import forms

class FormApp (forms.Form):
    name = forms.CharField (max_length=100, required=True, widget=forms.TextInput (attrs={'placeholder': 'Name ...', 'id': 'name'}))
    email = forms.EmailField (max_length=50, required=True, widget=forms.EmailInput (attrs={'placeholder': 'email ...', 'id':'email'}))
    phone = forms.IntegerField (widget=forms.NumberInput ({'placeholder': 'phone ...', 'id':'phone'}))
    commentary = forms.CharField (required=True, widget=forms.Textarea (attrs={'placeholder': 'commentary ...', 'id': 'comentary'}))