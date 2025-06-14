from typing import List, Any

from django.urls import path

from dontrack_pretix.views.pretix import PretixImportView

urlpatterns: List[Any] = [
    # donations
    path('<str:organizer>/<str:event>/<str:pseudo_id>', PretixImportView.as_view(), name="pretix_import"),
]
