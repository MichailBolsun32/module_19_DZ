from django import forms
from django.core.exceptions import ValidationError

def validate_age(value):
    if value > 999:
        raise ValidationError('Возраст не должен превышать трех знаков')

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(max_length=8, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст', validators=[validate_age])


