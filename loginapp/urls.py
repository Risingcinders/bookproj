from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    # path('success', views.success),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout)
]
