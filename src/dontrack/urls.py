"""
URL configuration for dontrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List, Any

from django.conf import settings
from django.urls import path, include

from dontrack.accounts.views.landing_page import LandingPageView

urlpatterns: List[Any] = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('donations/', include('dontrack.donations.urls')),
    path('donors/', include('dontrack.donors.urls')),
    path('log/', include('dontrack.log.urls')),
    path('user/', include('dontrack.accounts.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('qr-code/', include('qr_code.urls', namespace='qr-code')),
]

if settings.PRETIX_IMPORT:
    urlpatterns.append(path('don/', include('dontrack_pretix.urls')))