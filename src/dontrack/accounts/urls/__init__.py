from typing import Any, List

from django.urls import path

from dontrack.accounts.views.auth import AuthorizeSSOUser, UserLoginView, UserLogoutView


urlpatterns: List[Any] = [
    # auth
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # sso
    path('auth/', AuthorizeSSOUser.as_view(), name='auth'),
]

