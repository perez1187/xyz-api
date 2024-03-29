'''
    article:
        https://baronchibuike.medium.com/how-to-read-csv-file-and-save-the-content-to-the-database-in-django-rest-256c254ef722
'''
import pandas as pd
import numpy as np 
from pandas import Series, DataFrame
import json

from django.db.models import Count, Sum

from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import status, generics, filters, permissions

from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

from .models import Nickname, Club,ReportId, Result, AffAgent
from .serializers import FileUploadSerializer, ResultAdminSummarySerializer, ResultsSubmitSerializer, ReportsListSerializer #SaveFileSerializer
from .utils import checkClubExist, checkNicknameExist, newReportId, creatingNewResult, calculateClubResults, calculateResultsAdminV, calculateResultsPlayerV
from .utils import checkNicknameExistNick, creatingNewResultPDeals, checkClubExistManualyNicknames
# from .filters import ResultFilter

# from core_apps.nickname.models import Nickname

from .filters import ResultFilter

User = get_user_model()

# DSG reports
class UploadFileView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        reportName = newReportId() # creating new Report

        affAgentId = 1 # dsg id

        qs = Result.objects.all().values() # with columns
        all_results = pd.DataFrame(qs)
        print(all_results)

        # adding results to Result table
        for _, row in reader.iterrows():   

            club = row["CLUB"]
            nickname = row["NICKNAME"]

            clubId = checkClubExist(club,affAgentId) # check if club exist or create new club            
            checkNicknameExist(nickname, clubId, club,affAgentId) # check if nick exists or create new Nick
            
            creatingNewResult(clubId,reportName,row,affAgentId) # add new result

        return Response({"status":qs},
                        status.HTTP_201_CREATED)

# Pdeals reports
class UploadFilePDealsView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        reportName = newReportId() # creating new Report

        affAgentId = 2 # pdeals id

        qs = Result.objects.all().values() # with columns
        all_results = pd.DataFrame(qs)
        print(all_results)

        # adding results to Result table
        for _, row in reader.iterrows():   

            club = row["Club"]
            nickname = row["Nickname"]

            clubId = checkClubExist(club,affAgentId) # check if club exist or create new club            
            checkNicknameExist(nickname, clubId, club,affAgentId) # check if nick exists or create new Nick
            
            creatingNewResultPDeals(clubId,reportName,row,affAgentId) # add new result

        return Response({"status":qs},
                        status.HTTP_201_CREATED)                        

# as default affAgent ID = 1
class UploadNicknames(generics.CreateAPIView):
    
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        reader = pd.read_csv(file)

        print(reader)

        affAgentId = 1 # dsg id

        for _, row in reader.iterrows():   

            club = row["club"]
            nickname = row["nickname"]
            user = row["user"]
            player_TestRb = row["rb"]
            player_Testadjustment = row["adjustment"]



            clubId = checkClubExistManualyNicknames(club,affAgentId) # check if club exist or create new club            
            checkNicknameExistNick(nickname, clubId, club, user, player_TestRb, player_Testadjustment) # check if nick exists or create new Nick
            
            # creatingNewResult(clubId,reportName,row) # add new result


        return Response({"status":"ok"},
                status.HTTP_201_CREATED)


class ResultListAPIView(generics.ListAPIView):
    serializer_class = ResultAdminSummarySerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Result.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]    
    filterset_class = ResultFilter

# filter by:
# reportDate=YYYY-MM-DD (always should be sunday)
class PlayerResults(generics.ListAPIView):

    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        queryset = Result.objects.all()
        username = self.request.user
        reportDate = self.request.query_params.get('reportDate')

        queryset = queryset.filter(nickname__player__username=username)

        if reportDate is not None:
            queryset = queryset.filter(reportId__date=reportDate)  

        return queryset

    # overwriting list (get request)
    def list(self, request):

        queryset = self.get_queryset()     

        results = calculateResultsPlayerV(queryset)

        return Response({"playerResults" : results},status.HTTP_201_CREATED)

# filter by:
# reportDate=YYYY-MM-DD (always should be sunday)
# username=username
class AdminResultsView(generics.ListAPIView):

    permission_classes = [permissions.IsAdminUser]

    # overwriting query set
    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/
        queryset = Result.objects.all()
        username =   self.request.query_params.get('username')
        reportDate = self.request.query_params.get('reportDate')
        
        if username is not None:
            queryset = queryset.filter(nickname__player__username=username)

        if reportDate is not None:
            queryset = queryset.filter(reportId__date=reportDate)  

        return queryset

    # overwriting list (get request)
    def list(self, request):

        queryset = self.get_queryset()     

        results = calculateResultsAdminV(queryset)

        return Response({"Results" : results},status.HTTP_200_OK)

# filter by:
# reportDate=YYYY-MM-DD (always should be sunday)
class ClubResultsAdminView(generics.ListAPIView):
    
    permission_classes = [permissions.IsAdminUser,]

    def get_queryset(self):

        queryset = Result.objects.all()

        reportDate = self.request.query_params.get('reportDate')

        if reportDate is not None:
            queryset = queryset.filter(reportId__date=reportDate)  

        return queryset

    def list(self, request):

        queryset = self.get_queryset()

        results = calculateClubResults(queryset)

        return Response({"ClubResults" : results},status.HTTP_200_OK) 

# create report list for logged in users
class ReportsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = ReportId.objects.all()
    serializer_class = ReportsListSerializer
