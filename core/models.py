from django.db import models

from .choices import CATEGORY_CHOICES, URGENCY_CHOICES


class Job(models.Model):
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=120)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    matched_provider = models.ForeignKey(
        "providers.Provider",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="claimed_jobs",
    )
    matched_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.category} — {self.name} ({self.location})"

    @property
    def is_claimed(self):
        return self.matched_provider_id is not None
