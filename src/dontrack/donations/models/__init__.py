from auditlog.registry import auditlog

from .donation import Donation

auditlog.register(Donation)