from django import forms


class RegistroForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Digite seu nome'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Digite sua senha'}))
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Digite seu e-mail'}))
    tel = forms.CharField(max_length=100,
                          widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Digite seu telefone'}))
