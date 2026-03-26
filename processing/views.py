from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import ProcessingStage
from .forms import ProcessingStageForm


@login_required
def stage_list(request):
    stages = ProcessingStage.objects.select_related("batch").all()
    return render(request, "processing/stage_list.html", {"stages": stages})


@login_required
@user_passes_test(lambda user: user.is_staff)
def stage_create(request):
    if request.method == "POST":
        form = ProcessingStageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stage_list")
    else:
        form = ProcessingStageForm()
    return render(request, "processing/stage_form.html", {"form": form})

# Create your views here.
