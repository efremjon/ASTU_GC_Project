from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login_view, name="login"),
    path('log_out', views.logout_view, name="logout"),
    path('Create_SuperUser/', views.SuperUser_CreateView, name="register"),

    #password reseting area
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
