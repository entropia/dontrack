from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView
from pydantic import UUID4

from dontrack.donations.models import Donation

class DonationCreateView(LoginRequiredMixin, CreateView):
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
    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        return super(DonationCreateView, self).form_valid(form)

    def get_success_url(self):
         return reverse_lazy('donor_qr', kwargs={'pk': self.pk})

class DonationListView(LoginRequiredMixin, ListView):
    model = Donation
    object: Donation
    extra_context = {
        'title': _('Donations'),
    }
    permission_required = 'donations.view_donation'
    template_name = 'donations/donation_list.html'

class DonationExportView(LoginRequiredMixin, ListView):
    model = Donation
    object: Donation
    permission_required = 'donations.view_donation'
    template_name = 'donations/donation_list.json'