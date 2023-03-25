from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/results/", include("core_apps.results.urls")),
    path("api/v1/settlement/", include("core_apps.settlement.urls")),
]

admin.site.site_header = "Settlements"
admin.site.site_title = "Settlements API Admin Portal"
admin.site.index_title = "Settlements API Portal"