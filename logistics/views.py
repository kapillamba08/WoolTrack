from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import DistributionEvent
from .forms import DistributionEventForm


@login_required
def event_list(request):
    events = DistributionEvent.objects.select_related("batch").all()
    return render(request, "logistics/event_list.html", {"events": events})


@login_required
@user_passes_test(lambda user: user.is_staff)
def event_create(request):
    if request.method == "POST":
        form = DistributionEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = DistributionEventForm()
    return render(request, "logistics/event_form.html", {"form": form})

# Create your views here.
