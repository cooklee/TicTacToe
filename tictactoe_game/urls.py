from django.urls import path, include
from rest_framework import routers
from tictactoe_game import views

router = routers.DefaultRouter()
router.register(r'game', views.GameViewSet)
router.register(r'move', views.MoveViewSet)
# router.register(r'cash_move', views.CashMoveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]