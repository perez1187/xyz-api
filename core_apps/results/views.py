'''
    article:
        https://baronchibuike.medium.com/how-to-read-csv-file-and-save-the-content-to-the-database-in-django-rest-256c254ef722
'''
import pandas as pd
import numpy as np 
from pandas import Series, DataFrame
import json

from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import status, generics, filters, permissions

from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

from .models import Nickname, Club,ReportId, Result
from .serializers import FileUploadSerializer, ResultAdminSummarySerializer, ResultsSubmitSerializer #SaveFileSerializer
from .utils import checkClubExist, checkNicknameExist, newReportId, creatingNewResult, calculateResults
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

        qs = Result.objects.all().values() # with columns
        all_results = pd.DataFrame(qs)
        print(all_results)
        
        # qs2 = Result.objects.all().values_list() # without columns
        # all_results2 = pd.DataFrame(qs2)
        # print(all_results2)

        # adding results to Result table
        for _, row in reader.iterrows():   

            club = row["CLUB"]
            nickname = row["NICKNAME"]

            clubId = checkClubExist(club) # check if club exist or create new club            
            checkNicknameExist(nickname, clubId, club) # check if nick exists or create new Nick
            
            creatingNewResult(clubId,reportName,row) # add new result

        return Response({"status":qs},
                        status.HTTP_201_CREATED)

class ResultListAPIView(generics.ListAPIView):
    serializer_class = ResultAdminSummarySerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Result.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]    
    filterset_class = ResultFilter


class PlayerResults(generics.ListAPIView):
    
    serializer_class = ResultAdminSummarySerializer
    # permission_classes = [permissions.IsAdminUser]


    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        queryset = Result.objects.all()
        username = self.request.user
        reportId = self.request.query_params.get('reportId')

        queryset = queryset.filter(nickname__player__username=username)

        if reportId is not None:
            queryset = queryset.filter(reportId__pk=reportId)  

        return queryset

    # overwriting list (get request)
    def list(self, request):
         # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()     
        serializer = ResultAdminSummarySerializer(queryset,many=True)

        df = pd.DataFrame(serializer.data) # dataframe

        try:
            allResults = calculateResults(df)
        except:
            return Response({"Results":"no results"},status.HTTP_200_OK)

        return Response({"playerResults" : allResults},status.HTTP_201_CREATED)

class AdminResultsView(generics.ListAPIView):
    
    serializer_class = ResultAdminSummarySerializer
    permission_classes = [permissions.IsAdminUser]


    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        queryset = Result.objects.all()
        username =   self.request.query_params.get('username')
        reportId = self.request.query_params.get('reportId')
        
        if username is not None:
            queryset = queryset.filter(nickname__player__username=username)

        if reportId is not None:
            queryset = queryset.filter(reportId__pk=reportId)  
             
        # print("uuuuuuuuuuuuuuuuuuuuuuuuser",username)
        # print(queryset)

        return queryset

    # overwriting list (get request)
    def list(self, request):
         # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()     
        serializer = ResultAdminSummarySerializer(queryset,many=True)

        df = pd.DataFrame(serializer.data) # dataframe

        try:
            allResults = calculateResults(df)
        except:
            return Response({"Results":"no results"},status.HTTP_200_OK)
        return Response({"Results" : allResults},status.HTTP_200_OK)