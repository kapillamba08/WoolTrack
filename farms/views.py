from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import Farm
from .forms import FarmForm


@login_required
def farm_list(request):
    farms = Farm.objects.all()
    return render(request, "farms/farm_list.html", {"farms": farms})


@login_required
@user_passes_test(lambda user: user.is_staff)
def farm_create(request):
    if request.method == "POST":
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("farm_list")
    else:
        form = FarmForm()
    return render(request, "farms/farm_form.html", {"form": form})

# Create your views here.
