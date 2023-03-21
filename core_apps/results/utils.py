from datetime import datetime

from .models import Club, Nickname, ReportId, Result

import pandas as pd
import numpy as np 
from pandas import Series, DataFrame
import json


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
        # print("jest", clubId)
        return clubId
    else:
        # save a new club
        # print("nie ma")
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


def calculateResults(df) :

    df['profit_loss'] = pd.to_numeric(df['profit_loss'])
    df['rake'] = pd.to_numeric(df['rake'])

    # playerResult = df.groupby(['nickname','club'])['profit_loss','rake'].sum()
    # df2 = playerResult.to_json(orient ='index') #'values'
    # print(playerResult)
    # print(json.loads(df2))

    playerResultsGrouped = df.groupby(
            [
                'nickname',
                'club'
                ]
        ).agg(
            {
                'profit_loss':'sum',
                'rake':'sum',
                'player_rb':'mean',
                'player_adjustment':'mean'
                })

    df3 = playerResultsGrouped.to_json(orient ='index')
    # print(playerResultsGrouped)
    
    allTempResults = json.loads(df3)
    return allTempResults    