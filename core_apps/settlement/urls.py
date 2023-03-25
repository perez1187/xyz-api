from django.urls import path


from .views import PlayerSettlementView, PlayerSettlementAdminView

urlpatterns = [
    path('player/', PlayerSettlementView.as_view(), name='playerSettlement'),
    path('admin/player/', PlayerSettlementAdminView.as_view(), name='playerSettlement'),

]