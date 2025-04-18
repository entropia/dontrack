from auditlog.models import LogEntry

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _

class LogView(LoginRequiredMixin, ListView):
    model = LogEntry
    object: LogEntry
    extra_context = {
        'title': _('Auditlog'),
    }
    template_name = 'log/log_list.html'

