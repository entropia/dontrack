from auditlog.registry import auditlog

from .donor import Donor

auditlog.register(Donor)
