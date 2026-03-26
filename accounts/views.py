from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    """Allow a new user to create an account and log in immediately."""
    if request.user.is_authenticated:
        messages.info(request, "You are already signed in.")
        return redirect("dashboard_home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to WoolTrack! Your account is ready.")
            return redirect("dashboard_home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
