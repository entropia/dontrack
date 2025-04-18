from typing import Any, List

from django.urls import path

from dontrack.log.views.log import LogView


urlpatterns: List[Any] = [
    # log
    path("", LogView.as_view(), name="log_list"),
]