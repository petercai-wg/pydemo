from django.urls import include, path

from .views import MyTokenObtainPairView, getUserAccess, chatroom

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("useraccess/", getUserAccess, name="getUserAccess"),
    path("chatroom/<str:room_name>/", chatroom, name="chatroom"),
]
