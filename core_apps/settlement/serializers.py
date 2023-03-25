from rest_framework import serializers

from .models import Settlement

class SettlementSerializer(serializers.ModelSerializer):

    player = serializers.ReadOnlyField(source="player.username") # otherwise id
    
    class Meta:
        model= Settlement
        fields= "__all__"