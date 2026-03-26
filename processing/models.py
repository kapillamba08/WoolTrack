from django.db import models


class ProcessingStage(models.Model):
    class StageType(models.TextChoices):
        SCOURING = "SCOURING", "Scouring"
        CARDING = "CARDING", "Carding"
        SPINNING = "SPINNING", "Spinning"
        DYEING = "DYEING", "Dyeing"
        WEAVING = "WEAVING", "Weaving"
        FINISHING = "FINISHING", "Finishing"

    class StageStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"
        FAILED = "FAILED", "Failed"

    batch = models.ForeignKey("batches.WoolBatch", on_delete=models.CASCADE, related_name="processing_stages")
    stage_type = models.CharField(max_length=20, choices=StageType.choices)
    facility = models.CharField(max_length=200)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StageStatus.choices, default=StageStatus.PENDING)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self) -> str:
        return f"{self.stage_type} ({self.status}) - {self.batch.batch_id}"
