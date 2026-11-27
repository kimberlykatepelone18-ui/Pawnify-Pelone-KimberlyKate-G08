from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
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


@login_required
def home(request):          # temporary, replaced in Branch 2
    return render(request, 'home.html')