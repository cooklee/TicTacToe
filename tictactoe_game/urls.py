from django.urls import path, include
from rest_framework import routers

from tictactoe_game import views

router = routers.DefaultRouter()
router.register(r'game', views.GameViewSet)
router.register(r'move', views.MoveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('highscore/', views.HighScoreView.as_view())
]
