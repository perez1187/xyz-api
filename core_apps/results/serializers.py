from rest_framework import serializers

from .models import Result,ReportId

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
# class SaveFileSerializer(serializers.Serializer):
    
#     class Meta:
#         model = Result
#         fields = "__all__"


class ResultAdminSummarySerializer(serializers.ModelSerializer):
    
    player = serializers.ReadOnlyField(source="nickname.player.username")
    nickname = serializers.ReadOnlyField(source="nickname.nickname") # this is what I added
    player_rb = serializers.ReadOnlyField(source="nickname.player_rb")
    player_adjustment = serializers.ReadOnlyField(source="nickname.player_adjustment")
    club = serializers.ReadOnlyField(source="club.club")
    reportId = serializers.ReadOnlyField(source="reportId.date") 

    class Meta:
        model = Result
        fields = "__all__"

# get player results
# # later add restriction (only 'owner' or admin)        

class ResultsSubmitSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source="nickname.player.username")

    class Meta:
        model = Result
        fields = ("player",)

class ReportsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportId
        fields = [
            "id",            
            "date",
        ]