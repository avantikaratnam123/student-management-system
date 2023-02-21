from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup),
    path('courses',views.courses),
    path('dashboard',views.dashboard),
    path('employees',views.employees),
    path('index',views.index),
    path('notifications',views.notifications),
    path('pg_dashboard',views.pg_dashboard),
    path('profile',views.profile),
    path('tables',views.tables),
    path('tenants',views.tenants),
    path('viewstudents',views.viewstudents),
    path('signupdata/',views.signupdata),
    path('logindata/',views.logindata),

]
