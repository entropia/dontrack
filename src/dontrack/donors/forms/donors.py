from django.forms import ModelForm

from dontrack.donors.models import Donor


class DonorRegistrationForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'email', 'street', 'postal_code', 'city', 'country']