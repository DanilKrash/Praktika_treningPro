from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from authapp.models import Attendance, Sport, Trainer, Contact


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Логин'}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Почта'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={"class": "form-control mt-2", "placeholder": "Логин"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={"class": "form-control mt-2", "placeholder": "Пароль"}))


class AttendanceForm(forms.ModelForm):
    login = forms.DateTimeField(label='', widget=forms.DateTimeInput(
        attrs={"class": "form-select mt-2", 'type': 'datetime-local', "placeholder": "Начало"}))
    logout = forms.DateTimeField(label='', widget=forms.DateTimeInput(
        attrs={"class": "form-control mt-2", 'type': 'datetime-local', "placeholder": "Конец"}))
    sport = forms.ModelChoiceField(label='', queryset=Sport.objects.all(), widget=forms.Select(
        attrs={"class": "form-select mt-2", "placeholder": "Вид спорта"}))
    trainer = forms.ModelChoiceField(label='', queryset=Trainer.objects.all(),
                                     widget=forms.Select(attrs={"class": "form-select mt-2"}))

    class Meta:
        model = Attendance
        fields = ('login', 'logout', 'sport', 'trainer')


class ContactForm(ModelForm):
    body = forms.CharField(label='',
                           widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': 'Описание'}))

    class Meta:
        model = Contact
        fields = ('body',)
