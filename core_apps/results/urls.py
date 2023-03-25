from django.urls import path
from .views import UploadFileView, ResultListAPIView, PlayerResults, AdminResultsView, ClubResultsAdminView
# from .views import UploadFileView,ResultsListsAPIView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('results/',PlayerResults.as_view(),name="testres"),
    path('admin/results/',AdminResultsView.as_view(),name="testresas"),
    path('admin/club/results/',ClubResultsAdminView.as_view(),name="testresas"),
]