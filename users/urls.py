from django.contrib.auth import views
from django.urls import path
from users.views import RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
