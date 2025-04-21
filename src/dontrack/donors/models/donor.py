from __future__ import annotations

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Donor(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name'))

    email = models.EmailField(null=False, blank=False, verbose_name=_('Email'))

    street = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Street'))
    postal_code = models.CharField(max_length=8, null=False, blank=False, verbose_name=_('Postal code'))
    city = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('City'))
    country = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Country'))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Donor")
        verbose_name_plural = _("Donors")
        default_permissions = ()
