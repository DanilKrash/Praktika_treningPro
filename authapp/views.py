from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authapp.forms import RegisterUserForm, LoginUserForm, AttendanceForm, ContactForm, ProfileForm
from authapp.models import Contact, Attendance, Sport, Profile


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


def sport(request):
    tren = Sport.objects.all()
    return render(request, "sport.html", {'tren': tren})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')

    prof = Profile.objects.filter(user=request.user)
    attend = Attendance.objects.filter(user=request.user)
    return render(request, "profile.html", {'attend': attend, 'prof': prof})


def profile_create(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')

    form_prof = ProfileForm(request.POST, request.FILES)
    if form_prof.is_valid():
        form = form_prof.save(commit=False)
        form.user = request.user
        form.save()
        form_prof.save_m2m()
        return redirect('/profile')
    else:
        form = ProfileForm()
    return render(request, "create_profile.html", {'form': form})


def profile_update(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, "Пожалуйста, войдите и попробуйте заново")
        return redirect('/login')

    prof = get_object_or_404(Profile, id=id)
    form_prof = ProfileForm(request.POST, request.FILES, instance=prof)
    if form_prof.is_valid():
        form = form_prof.save(commit=False)
        form.user = request.user
        form.save()
        form_prof.save_m2m()
        return redirect('/profile')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "prof": prof})


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


def attendance_view(request, id):
    attend_det = get_object_or_404(Attendance, id=id)
    return render(request, "detail_attendance.html", {'attend_det': attend_det})

# class StatusUpdateView(UpdateView):
#     model = Application
#     template_name = 'account/status_update.html'
#     success_url = '/account/'
#     form_class = UpdateStatusForm


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
            return redirect('/contact')

    form = ContactForm()
    return render(request, "contact.html", {'form': form, 'cont': cont})
