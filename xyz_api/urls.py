from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/results/", include("core_apps.results.urls")),
    path("api/v1/settlement/", include("core_apps.settlement.urls")),
    path("api/v1/users/", include("core_apps.users.urls")),
]

admin.site.site_header = "Fish Hunters Portal"
admin.site.site_title = "Fish Hunters Portal"
admin.site.index_title = "Fish Hunters Portal"