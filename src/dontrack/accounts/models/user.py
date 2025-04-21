from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser, Permission
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from dontrack import settings

if TYPE_CHECKING:
    pass

class BaseUser(AbstractUser):
    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.display

    @property
    def display(self) -> str:
        if hasattr(self, 'user'):
            return self.user.display
        return self.get_full_name()

class User(BaseUser):
    display_name = models.CharField(max_length=150, verbose_name=_('Display name'), null=True, blank=True)

    class Meta:
        default_permissions = ()
        ordering = ['username']

    def __str__(self) -> str:
        return f'{self.display_name}'

    @property
    def is_executive(self) -> bool:
        return self.groups.filter(name=settings.OAUTH_ADMIN_GROUP).exists()

    @property
    def is_registration(self) -> bool:
        return self.groups.filter(name=settings.OAUTH_STAFF_GROUP).exists()

    def get_absolute_url(self) -> str:
        return reverse('user_profile')

    def has_perm(self, perm, obj=None) -> bool:
        if not self.is_active:
            return False
        for group in self.groups.all():
            try:
                if perm in settings.permissions[group.name]:
                    return True
            except KeyError:
                pass
        return False

    # Is no used
    def has_module_perms(self, app_label: str) -> bool:
        return False