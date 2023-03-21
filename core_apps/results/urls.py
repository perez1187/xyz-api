from django.urls import path
from .views import UploadFileView, ResultListAPIView, PlayerResults, AdminResultsView
# from .views import UploadFileView,ResultsListsAPIView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    # path('results/', ResultListAPIView.as_view(), name='results'),
    path('results/',PlayerResults.as_view(),name="testres"),
    path('adminresults/',AdminResultsView.as_view(),name="testresas"),
]