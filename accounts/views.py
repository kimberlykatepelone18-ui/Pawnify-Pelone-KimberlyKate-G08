from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from .decorators import role_required
from .forms import RegistrationForm
from .models import User

def register(request):
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
        messages.error(request, 'Please correct the errors below.')
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Welcome back, {user.first_name or user.username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse(self.request.user.get_dashboard_url())


@login_required
def dashboard_redirect(request):
    return redirect(request.user.get_dashboard_url())


@role_required(User.Role.ADMIN)
def admin_dashboard(request):
    return render(request, 'dashboards/admin.html')


@role_required(User.Role.APPRAISER)
def appraiser_dashboard(request):
    return render(request, 'dashboards/appraiser.html')


@role_required(User.Role.CASHIER)
def cashier_dashboard(request):
    return render(request, 'dashboards/cashier.html')


@role_required(User.Role.CUSTOMER)
def customer_dashboard(request):
    return render(request, 'dashboards/customer.html')