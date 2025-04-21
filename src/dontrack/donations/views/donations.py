from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView
from pydantic import UUID4

from dontrack.donations.models import Donation

class DonationCreateView(PermissionRequiredMixin, CreateView):
    def __init__(self):
        super().__init__()
        self.pk: Optional[UUID4] = None
    model = Donation
    object: Donation
    extra_context = {
        'title': _('Create donation'),
    }
    fields = [
        'amount',
    ]
    template_name = 'donations/donation_create.html'
    success_url = reverse_lazy('donation_create')
    permission_required = 'donations.register_donation'
    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        return super(DonationCreateView, self).form_valid(form)

    def get_success_url(self):
         return reverse_lazy('donor_qr', kwargs={'pk': self.pk})

class DonationListView(PermissionRequiredMixin, ListView):
    model = Donation
    object: Donation
    extra_context = {
        'title': _('Donations'),
    }
    permission_required = 'donations.list_donations'
    template_name = 'donations/donation_list.html'

class DonationExportView(PermissionRequiredMixin, ListView):
    model = Donation
    object: Donation
    permission_required = 'donations.list_donations'
    template_name = 'donations/donation_list.json'