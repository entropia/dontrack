from typing import Any, List

from django.urls import path

from dontrack.donors.views.donors import DonorQRView, DonorRegistrationView, DonorRegistrationSuccessView

urlpatterns: List[Any] = [
    # donations
    path('qr/<uuid:pk>', DonorQRView.as_view(), name="donor_qr"),
    path('register/<uuid:pk>', DonorRegistrationView.as_view(), name="donor_registration"),
    path('register/success', DonorRegistrationSuccessView.as_view(), name="donor_registration_success"),
]
