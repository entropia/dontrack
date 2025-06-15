from __future__ import annotations

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order_id = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Pretix order id'))
    position_id = models.IntegerField(null=False, blank=False, verbose_name=_('Pretix position id'))

    donation = models.ForeignKey('donations.Donation', null=False, on_delete=models.CASCADE, related_name="pretix_orders",
                              verbose_name=_("Donation"))

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Pretix order")
        verbose_name_plural = _("Pretix orders")
        default_permissions = ()
        unique_together = ("order_id", "position_id")


    def __str__(self) -> str:
        return f'Pretix order {self.order_id} ({self.position_id})'
