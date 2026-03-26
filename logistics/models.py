from django.db import models


class DistributionEvent(models.Model):
    class EventType(models.TextChoices):
        SHIPMENT = "SHIPMENT", "Shipment"
        RECEIPT = "RECEIPT", "Receipt"
        WAREHOUSE = "WAREHOUSE", "Warehouse"
        RETAIL = "RETAIL", "Retail"

    batch = models.ForeignKey("batches.WoolBatch", on_delete=models.CASCADE, related_name="distribution_events")
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return f"{self.event_type} - {self.batch.batch_id} @ {self.location}"
