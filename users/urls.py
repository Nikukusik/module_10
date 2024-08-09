from django.contrib.auth import views
from django.urls import path
from users.views import RegisterView, ResetPasswordView
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('reset_password/',
         ResetPasswordView.as_view(template_name='users/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
