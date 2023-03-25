from rest_framework import generics, permissions

from .serializers import SettlementSerializer
from .models import Settlement

class PlayerSettlementView(generics.ListAPIView):
    
    serializer_class= SettlementSerializer

    def get_queryset(self):
        queryset = Settlement.objects.all()
        username = self.request.user

        queryset = queryset.filter(player__username=username)

        return queryset

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = SettlementSerializer(queryset, many=True)

class PlayerSettlementAdminView(generics.ListAPIView):
    
    serializer_class= SettlementSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Settlement.objects.all()
        username =   self.request.query_params.get('username')

        if username is not None:
            queryset = queryset.filter(player__username=username)

        return queryset
