from datetime import datetime
from django.db.models import Count, Sum
from django.contrib.auth import get_user_model

from .models import Club, Nickname, ReportId, Result

import pandas as pd
import numpy as np 
from pandas import Series, DataFrame
import json

User = get_user_model()

def newReportId():
    reportName = str(datetime.now())
    newReport = ReportId(
        name=reportName
    )

    newReport.save()

    return reportName


def checkClubExist(club):
    
    if Club.objects.filter(club=club).exists():
        clubId = Club.objects.get(club=club).pk
        print("jest", clubId)
        return clubId
    else:
        # save a new club
        print("nie ma clubu")
        new_club = Club(
            club=club
        )
        new_club.save()

        clubId = Club.objects.get(club=club).pk
        # print("saved",clubId)
        return clubId

def checkNicknameExist(nickname, clubId, club):
        
        if Nickname.objects.filter(nickname = nickname,club=clubId).exists():
            print("Nick istnieje")
            return

        else:
            print("Nicka nie ma")
            # save nick
            new_nickname = Nickname(
                nickname = nickname,
                club=Club.objects.get(club=club),
                # player = 5
            )
            new_nickname.save()
            return

# method for adding existing nicknames
def checkNicknameExistNick(nickname, clubId, club, user, player_TestRb, player_adjustment):
        
        if Nickname.objects.filter(nickname = nickname,club=clubId).exists():
            print("Nick istnieje")
            return

        else:
            # print("Nicka nie ma")

            if User.objects.filter(pkid = user).exists():
                print("mogę zapisac nick: " + nickname + "from user: " + str(user))
                            # save nick
                new_nickname = Nickname(
                    nickname = nickname,
                    club=Club.objects.get(club=club),
                    player = User.objects.get(pk=user),
                    player_rb=player_TestRb,
                    player_adjustment=player_adjustment
                )
                new_nickname.save()

            else:
                print(" NIEEE nick " + nickname + "bo user " + str(user))
                print(type(player_TestRb) )
                # save nick
                new_nickname = Nickname(
                    nickname = nickname,
                    club=Club.objects.get(club=club),
                    player = User.objects.get(pk=2),
                    player_rb=player_TestRb,
                    player_adjustment=player_adjustment
                )
                new_nickname.save()
            return

# def creatingNewResult(nickname,clubId,reportName,club, agents,profit_loss,rake,deal,rakeback,adjustment,agent_settlement):
def creatingNewResult(clubId,reportName,row):
    club = row["CLUB"]
    nickname = row["NICKNAME"]
    agents=row["AGENTS"]
    profit_loss=row["PROFIT/LOSS"]
    rake=row["RAKE"]
    deal=row["DEAL"]
    rakeback=row["RAKEBACK"]
    adjustment=row["ADJUSTMENT"]
    agent_settlement=row["AGENT SETTLEMENT"]
    
    new_result = Result(
        nickname=Nickname.objects.get(nickname = nickname,club=clubId),
        reportId=ReportId.objects.get(name=reportName),
        club= Club.objects.get(club=club),
        agents=agents,
        profit_loss=profit_loss,
        rake=rake,
        deal=deal,
        rakeback=row["RAKEBACK"],
        adjustment=row["ADJUSTMENT"],
        agent_settlement=row["AGENT SETTLEMENT"],
    )
    new_result.save()

# .values -> show values, that will be shown, we can use multiple value .values('club__club', 'nickname')
# using __ (club__club) we can see str representation, otherwise we see ID
# .order_by is filtering, we can filter multiple fields, and we can create subquries
# . annotate, like in pivot table, we show results
# queryset is from def get_queryset()
# https://stackoverflow.com/questions/66819636/how-to-add-a-second-annotation-to-an-already-annotated-queryset-with-django-mode
# https://stackoverflow.com/questions/27180190/django-using-objects-values-and-get-foreignkey-data-in-template
def calculateClubResults(queryset):

    result= queryset.values(
        'club__club', 
        'nickname__nickname'
    ).order_by(
        'club',
        'nickname'
    ).annotate(
        total_profit=Sum('profit_loss'),
        total_rb=Sum('rake')
        )

    return result

# .values -> show values, that will be shown, we can use multiple value .values('club__club', 'nickname')
# using __ (club__club) we can see str representation, otherwise we see ID
# .order_by is filtering, we can filter multiple fields, and we can create subquries
# . annotate, like in pivot table, we show results
# queryset is from def get_queryset()
# https://stackoverflow.com/questions/66819636/how-to-add-a-second-annotation-to-an-already-annotated-queryset-with-django-mode
# https://stackoverflow.com/questions/27180190/django-using-objects-values-and-get-foreignkey-data-in-template
def calculateResultsAdminV(queryset):
    
    result= queryset.values(
        'nickname__player__username',
        'nickname__nickname',
        'club__club', 
    ).order_by(
        'club',
        'nickname'
    ).annotate(
        total_profit=Sum('profit_loss'),
        total_rb=Sum('rake')
        )

    return result

# .values -> show values, that will be shown, we can use multiple value .values('club__club', 'nickname')
# using __ (club__club) we can see str representation, otherwise we see ID
# .order_by is filtering, we can filter multiple fields, and we can create subquries
# . annotate, like in pivot table, we show results
# queryset is from def get_queryset()
# https://stackoverflow.com/questions/66819636/how-to-add-a-second-annotation-to-an-already-annotated-queryset-with-django-mode
# https://stackoverflow.com/questions/27180190/django-using-objects-values-and-get-foreignkey-data-in-template
def calculateResultsPlayerV(queryset):
   
    result= queryset.values(
        'nickname__player__username',
        'nickname__nickname',
        'club__club', 
        # 'reportId__date'
    ).order_by(
        'club',
        'nickname'
    ).annotate(
        total_profit=Sum('profit_loss'),
        total_rb=Sum('rake')
        )

    return result        