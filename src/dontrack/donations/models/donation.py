from __future__ import annotations

import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Donation(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_("Amount"), validators=[MinValueValidator(0)])

    donor = models.ForeignKey('donors.Donor', null=True, on_delete=models.CASCADE, related_name="donations",
                              verbose_name=_("Donor"))

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")
        default_permissions = ()
        permissions = [
            ('register_donation', 'May register donations'), ('list_donations', 'May list donations'),
        ]

    def __str__(self) -> str:
        if self.donor is None:
            return f'Unclaimed donation {self.amount} €'

        return f'Donation {self.amount} of {self.donor.name}'
