'''
    article:
        https://baronchibuike.medium.com/how-to-read-csv-file-and-save-the-content-to-the-database-in-django-rest-256c254ef722
'''


from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import status, generics, filters, permissions

from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

from .models import Nickname, Club,ReportId, Result
from .serializers import FileUploadSerializer# SaveFileSerializer, ResultSerializer
from .utils import checkClubExist, checkNicknameExist, newReportId, creatingNewResult
# from .filters import ResultFilter

# from core_apps.nickname.models import Nickname

from .filters import ResultFilter

User = get_user_model()

class UploadFileView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        reportName = newReportId() # creating new Report

        # adding results to Result table
        for _, row in reader.iterrows():   

            club = row["CLUB"]
            nickname = row["NICKNAME"]

            clubId = checkClubExist(club) # check if club exist or create new club            
            checkNicknameExist(nickname, clubId, club) # check if nick exists or create new Nick
            
            creatingNewResult(clubId,reportName,row) # add new result

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

# class ResultListAPIView(generics.ListAPIView):
#     serializer_class = ResultSerializer
#     permission_classes = [permissions.IsAdminUser]
#     queryset = Result.objects.all()
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]    
#     filterset_class = ResultFilter

# class ResultUserAPIView(generics.RetrieveAPIView)