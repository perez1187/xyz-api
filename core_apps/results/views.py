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

from .models import Result
from .serializers import FileUploadSerializer, SaveFileSerializer, ResultSerializer
# from .filters import ResultFilter

# from core_apps.nickname.models import Nickname
from .models import Nickname, Club
from .filters import ResultFilter

class UploadFileView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        # print("dziala")

        # adding results to Result table
        for _, row in reader.iterrows():   

            club = row["CLUB"]
            nickname = row["NICKNAME"]

            # check if club exist
            if Club.objects.filter(club=club).exists():
                clubId = Club.objects.get(club=club).pk
                print("jest", clubId)
            else:
                # save a new club
                print("nie ma")
                new_club = Club(
                    club=club
                )
                new_club.save()

                clubId = Club.objects.get(club=club).pk
                print("saved",clubId)

            # check if nick exists
            if Nickname.objects.filter(nickname = nickname,club=clubId).exists():
                print("Nick istnieje")


            else:
                print("Nicka nie ma")
                # save nick
                new_nickname = Nickname(
                    nickname = row["NICKNAME"],
                    club=Club.objects.get(club=club),
                    # player = 5
                )
                new_nickname.save()

                ''' dodac walidacje do results'''

            # new_result = Result(
            #     # player=Nickname.objects.get(nickname = nickname,club=clubId),
            #     nickname=Nickname.objects.get(nickname = nickname,club=clubId),
            #     # club= Nickname.objects.get(nickname = nickname,club=clubId)
            # )
            # new_result.save()
            nickname=Nickname.objects.get(nickname = nickname,club=clubId)

            ''' this is how to take username from nick'''
            testResult=Result.objects.get(nickname=nickname)
            print(testResult.nickname.player)


        # for _, row in reader.iterrows():

        #     # najpierw ID clubu

        #     if Nickname.objects.filter(nickname = row["NICKNAME"],club=row["CLUB"]).exists():

        #         nickname = Nickname.objects.get(nickname = row["NICKNAME"],club=row["CLUB"])
        #         new_file = Results(
        #                 nickname=nickname,
        #                 player=nickname.player,
        #                 club=nickname.club,
                        
        #                 # agents=row["AGENTS"],
        #                 # profit_loss=row["PROFIT/LOSS"],
        #                 # rake=row["RAKE"],
        #                 # deal=row["DEAL"],
        #                 # rakeback=row["RAKEBACK"],
        #                 # adjustment=row["ADJUSTMENT"],
        #                 # agent_settlement=row["AGENT SETTLEMENT"],
        #                 # date=row["DATE"],
        #                 )
        #         new_file.save()
           
        #     else:
                
        #         # we create new nick& club with User: niezarejestrowany
        #         new_nickname = Nickname(
        #             nickname = row["NICKNAME"],
        #             club=row["CLUB"],
        #             # player = 5
        #         )
        #         new_nickname.save()

        #         # now we save
        #         nickname = Nickname.objects.get(nickname = row["NICKNAME"],club=row["CLUB"])
                
        #         new_file = Results(
        #                 nickname=nickname,
        #                 player=nickname.player,
        #                 club=nickname.club,
        #                 # agents=row["AGENTS"],
        #                 # profit_loss=row["PROFIT/LOSS"],
        #                 # rake=row["RAKE"],
        #                 # deal=row["DEAL"],
        #                 # rakeback=row["RAKEBACK"],
        #                 # adjustment=row["ADJUSTMENT"],
        #                 # agent_settlement=row["AGENT SETTLEMENT"],
        #                 # date=row["DATE"],
        #                 )
        #         new_file.save()


        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

class ResultListAPIView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Result.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]    
    filterset_class = ResultFilter

# class ResultUserAPIView(generics.RetrieveAPIView)