from typing import Any, List

from django.urls import path

from dontrack.accounts.views.auth import AuthorizeSSOUser, UserLoginView, UserLogoutView
from dontrack.accounts.views.profile import UserProfileView


urlpatterns: List[Any] = [
    # auth
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # profile
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    # sso
    path('auth/', AuthorizeSSOUser.as_view(), name='auth'),
]
