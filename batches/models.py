from django.db import models


class WoolBatch(models.Model):
    class BatchStatus(models.TextChoices):
        CREATED = "CREATED", "Created"
        IN_PROCESS = "IN_PROCESS", "In Process"
        PROCESSED = "PROCESSED", "Processed"
        DISTRIBUTING = "DISTRIBUTING", "Distributing"
        DELIVERED = "DELIVERED", "Delivered"

    batch_id = models.CharField(max_length=50, unique=True)
    farm = models.ForeignKey("farms.Farm", on_delete=models.CASCADE, related_name="batches")
    shear_date = models.DateField()
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)
    quality_grade = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=BatchStatus.choices, default=BatchStatus.CREATED)
    current_location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Batch {self.batch_id} - {self.status}"
