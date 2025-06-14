from typing import Any

from django.conf import settings
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from dontrack.donations.models import Donation
from dontrack_pretix.models.order import Order
from dontrack_pretix.utils.pretix_api import PretixApiClient


class PretixImportView(RedirectView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        api_client = PretixApiClient(settings.PRETIX_ROOT_URL, kwargs['organizer'], kwargs['event'], settings.PRETIX_API_KEYS[kwargs['organizer']])

        # Get eligible products
        product_ids = api_client.get_products_in_quota(settings.PRETIX_DONATION_QUOTA)

        # Retrieve order information
        order = api_client.get_orderpositions({'pseudonymization_id': kwargs['pseudo_id']})

        # There should only be one order returned. Expect tampering otherwise and abort
        if len(order) == 1 and order[0].get('item') in product_ids:
            # Check if order is already imported so redirect else import order
            try:
                registered_order = Order.objects.get(order_id=order[0].get('order'), position_id=order[0].get('positionid'))
                return HttpResponseRedirect(reverse_lazy('donor_registration', kwargs={'pk': registered_order.donation.pk}))
            except Order.DoesNotExist:
                donation = Donation.objects.create(amount=order[0].get('price'))
                Order.objects.create(order_id=order[0].get('order'), position_id=order[0].get('positionid'), donation=donation)
                return HttpResponseRedirect(reverse_lazy('donor_registration', kwargs={'pk': donation.pk}))
        else:
            return HttpResponseNotAllowed(permitted_methods='GET')
