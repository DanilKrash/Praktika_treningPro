from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from authapp import views
from authapp.views import RegisterUserView, LoginUserView

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name="logout"),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('create_profile/', views.profile_create, name="create_profile"),
    path('update/<int:id>/', views.profile_update, name="update_profile"),
    path('attendance/', views.attendance, name="attendance"),
    path('attendance/<int:id>/', views.attendance_view, name="attendance_view"),
    path('sport/', views.sport, name="sport"),
    path('trainer/', views.trainer, name="trainer"),
    path('trainer/<int:id>/', views.trainer_detail, name='trainer_detail'),
]
