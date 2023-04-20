from django.urls import path
from .views import UploadFileView, ResultListAPIView, PlayerResults, AdminResultsView, ClubResultsAdminView, UploadNicknames, ReportsListView, UploadFilePDealsView
# from .views import UploadFileView,ResultsListsAPIView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('uploadPdeals/', UploadFilePDealsView.as_view(), name='upload-file'),
    path('nicnknameupload/', UploadNicknames.as_view(), name='upload-file'),
    path('results/',PlayerResults.as_view(),name="testres"),
    path('admin/results/',AdminResultsView.as_view(),name="testresas"),
    path('admin/club/results/',ClubResultsAdminView.as_view(),name="testresas"),
    path('reports/',ReportsListView.as_view(),name="testresas2"),
]