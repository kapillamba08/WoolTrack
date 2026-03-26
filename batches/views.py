from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import WoolBatch
from .forms import WoolBatchForm


@login_required
def batch_list(request):
    batches = WoolBatch.objects.select_related("farm").all()
    return render(request, "batches/batch_list.html", {"batches": batches})


@login_required
@user_passes_test(lambda user: user.is_staff)
def batch_create(request):
    if request.method == "POST":
        form = WoolBatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("batch_list")
    else:
        form = WoolBatchForm()
    return render(request, "batches/batch_form.html", {"form": form})
