"""
URL configuration for data_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data_home.views import home, print123
from users.views import register
from search_accounts.views import request_accounts, request_accounts_model
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("print/", print123, name="print"),
    path("admin/", admin.site.urls),
    path("register/", register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("accounts/", request_accounts, name="request_accounts"),
    path("accounts_model/", request_accounts_model, name="request_accounts_model"),
]
