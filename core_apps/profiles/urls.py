from django.urls import path

from .views import (
    ProfileDetailAPIView,
    ProfileListAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path(
        "user/<str:username>/", ProfileDetailAPIView.as_view(), name="profile-details"
    ),

]
