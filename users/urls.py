from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy

from .views import UserUpdateView


app_name = 'users'

urlpatterns = [
    path(
        'login/', views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path(
        'reset/password-reset/',
        views.PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            email_template_name='users/password_reset_email.html',
            success_url=reverse_lazy('users:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password-reset-done/',
        views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path(
        'password-change/',
        login_required(views.PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done')
        )),
        name='password_change'
    ),
    path(
        'password-change-done/',
        login_required(views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        )),
        name='password_change_done'
    ),

    path(
        'update/<int:pk>/',
        login_required(UserUpdateView.as_view()),
        name='user_update'
    ),
]
