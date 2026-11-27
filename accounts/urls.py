from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard_redirect, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/appraiser/', views.appraiser_dashboard, name='appraiser_dashboard'),
    path('dashboard/cashier/', views.cashier_dashboard, name='cashier_dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
]