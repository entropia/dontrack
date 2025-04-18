from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from django.utils.translation import gettext_lazy as _

from dontrack.donations.models import Donation
from dontrack.donors.forms.donors import DonorRegistrationForm
from dontrack.donors.models import Donor


class DonorQRView(LoginRequiredMixin, TemplateView):
    template_name = 'donors/qr_view.html'
    def get(self, request, *args, **kwargs):
        context = {
            'registration_url': request.build_absolute_uri(reverse_lazy('donor_registration', kwargs=kwargs)),
            'title': _('Donor registration QR-Code'),
        }
        return TemplateResponse(request=request, template=self.template_name, context=context)

class DonorRegistrationView(CreateView):
    model = Donor
    form_class = DonorRegistrationForm
    success_url = reverse_lazy('donor_registration_success')

    def get(self, request, *args, **kwargs):
        donation_object = Donation.objects.get(pk=kwargs['pk'])
        if donation_object.donor is not None:
            messages.warning(request, _('Donor is already registered.'))
            return TemplateResponse(request=request, template='donors/empty_page.html', context={'title': _('Donor registration error')})
        else:
            context = {
                'title': _('Register donor'),
                'donation': donation_object,
                'form': DonorRegistrationForm,
            }
            return TemplateResponse(request=request, template='donors/donor_create.html', context=context)

    def post(self, request, *args, **kwargs):
        super(DonorRegistrationView, self).post(request, *args, **kwargs)
        donation = Donation.objects.get(pk=kwargs['pk'])
        donation.donor = self.object
        donation.save()
        return redirect('donor_registration_success')

class DonorRegistrationSuccessView(TemplateView):
    template_name = 'donors/donor_registration_succes.html'