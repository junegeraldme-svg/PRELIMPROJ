from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ConsultationForm
from .models import Consultation


# LOGIN PAGE
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'juney/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# HOME PAGE
@login_required
def home_view(request):
    return render(request, 'juney/home.html')


# DASHBOARD
@login_required
def dashboard_view(request):
    return render(request, 'juney/dashboard.html')


# MENTAL HEALTH AWARENESS
@login_required
def awareness_view(request):
    return render(request, 'juney/awareness.html')


# CONSULTATION PAGE (WITH FORM + DATABASE SAVE)
@login_required
def consultation_view(request):

    if request.method == 'POST':
        form = ConsultationForm(request.POST)

        if form.is_valid():
            Consultation.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                concern=form.cleaned_data['concern']
            )

            messages.success(request, "Your consultation request has been submitted.")
            return redirect('consultation')

    else:
        form = ConsultationForm()

    return render(request, 'juney/consultation.html', {'form': form})


# WELLNESS PROGRAMS PAGE
@login_required
def wellness_view(request):
    return render(request, 'juney/wellness.html')