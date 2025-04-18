from __future__ import annotations

import uuid

from typing import TYPE_CHECKING

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Donation(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    amount = models.DecimalField(decimal_places=2, max_digits=10)

    donor = models.ForeignKey('donors.Donor', null=True, on_delete=models.CASCADE, related_name="donations")

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")

    def __str__(self) -> str:
        if self.donor is None:
            return f'Unclaimed donation {self.amount} €'

        return f'Donation {self.amount} of {self.donor.name}'
