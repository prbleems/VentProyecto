# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from .views import LogoutGetView

app_name = 'users'

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutGetView.as_view(),                                      name='logout'),
    path('signup/', SignUpView.as_view(),                                          name='signup'),
]