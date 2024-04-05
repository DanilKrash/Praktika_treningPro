from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authapp.forms import RegisterUserForm, LoginUserForm, AttendanceForm, ContactForm
from authapp.models import Contact, Attendance, Sport


def home(request):
    return render(request, "index.html")


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/profile')

    form = AttendanceForm()
    return render(request, "attendance.html", {'form': form})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')
    prof = Attendance.objects.filter(user=request.user)
    return render(request, "profile.html", {'prof': prof})


def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')
    cont = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = ContactForm
            messages.info(request, "Спасибо за ваш отзыв! Наши сотрудники рассмотрят его в ближайшее время")
            return redirect('/profile')

    form = ContactForm()
    return render(request, "contact.html", {'form': form, 'cont': cont})


def sport(request):
    tren = Sport.objects.all()
    return render(request, "sport.html", {'tren': tren})
