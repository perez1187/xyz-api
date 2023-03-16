from rest_framework import serializers

# from .models import Result

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
# class SaveFileSerializer(serializers.Serializer):
    
#     class Meta:
#         model = Result
#         fields = "__all__"


# class ResultSerializer(serializers.ModelSerializer):
    
#     # player = serializers.ReadOnlyField(source="nickname.player.username")
#     # nickname = serializers.ReadOnlyField(source="nickname.nickname") # this is what I added
#     # player_rb = serializers.ReadOnlyField(source="player.player_rb")
#     # player_adjustment = serializers.ReadOnlyField(source="player.player_adjustment")

#     class Meta:
#         model = Result
#         fields = "__all__"

# get player results
# # later add restriction (only 'owner' or admin)        

