from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),

    # password reset urls
    path('reset-password',
         PasswordResetView.as_view(
            template_name='password_reset.html'
         ),
         name='reset_password'),
    path('reset-password-done',
         PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset-password/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset-password-complete',
         PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]