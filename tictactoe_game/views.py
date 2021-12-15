from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets

from tictactoe_game.models import Game, Move
from tictactoe_game.serializer import GameSerializer, MoveSerializer


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filterset_fields = {
        'name': ['icontains'],
    }


#
class MoveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

#
# class CashMoveViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = CashMove.objects.all()
#     serializer_class = CashMoveSerializer
#     filterset_fields = {
#         'name': ['icontains'],
#         'amount': ['exact', 'lte', 'gte'],
#         'type': ['exact'],
#         'budget': ['exact'],
#     }
