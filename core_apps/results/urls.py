from django.urls import path
from .views import UploadFileView, ResultListAPIView
# from .views import UploadFileView,ResultsListsAPIView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('results/', ResultListAPIView.as_view(), name='results'),
]