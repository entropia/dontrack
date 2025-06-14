from auditlog.registry import auditlog

from .order import Order

auditlog.register(Order)
