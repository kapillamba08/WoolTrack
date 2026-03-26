from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import models
import json
from batches.models import WoolBatch
from farms.models import Farm
from processing.models import ProcessingStage
from logistics.models import DistributionEvent


@login_required
def home(request):
    total_farms = Farm.objects.count()
    total_batches = WoolBatch.objects.count()
    in_process = WoolBatch.objects.filter(status=WoolBatch.BatchStatus.IN_PROCESS).count()
    delivered = WoolBatch.objects.filter(status=WoolBatch.BatchStatus.DELIVERED).count()

    stage_counts = list(
        ProcessingStage.objects.values("stage_type")
        .order_by()
        .annotate(count=models.Count("id"))
    )
    event_counts = list(
        DistributionEvent.objects.values("event_type")
        .order_by()
        .annotate(count=models.Count("id"))
    )

    context = {
        "total_farms": total_farms,
        "total_batches": total_batches,
        "in_process": in_process,
        "delivered": delivered,
        "stage_counts": json.dumps(stage_counts),
        "event_counts": json.dumps(event_counts),
    }
    return render(request, "dashboard/home.html", context)

# Create your views here.
