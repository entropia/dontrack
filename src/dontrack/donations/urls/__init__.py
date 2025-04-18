from typing import Any, List

from django.urls import path

from dontrack.donations.views.donations import DonationCreateView, DonationExportView, DonationListView
urlpatterns: List[Any] = [
    # donations
    path('list', DonationListView.as_view(), name="donation_list"),
    path('export', DonationExportView.as_view(), name="donation_export"),
    path('create', DonationCreateView.as_view(),name='donation_create'),
]

