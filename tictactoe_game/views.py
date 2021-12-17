from django.contrib.auth import get_user_model
from django.db.models import Count
# Create your views here.
from rest_framework import permissions, viewsets, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from tictactoe_game.models import Game, Move
from tictactoe_game.serializer import GameSerializer, MoveSerializer, HighScoreSerializer


class GameViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.action == 'make_move':
            return MoveSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        game = serializer.save()
        game.set_current_player()

    @action(methods=['post'], detail=True)
    def make_move(self, request, pk):
        move_serializer = MoveSerializer(data=request.data, context=self.get_serializer_context())
        if move_serializer.is_valid():
            current_game = Game.objects.get(pk=pk)
            move = move_serializer.save(game=current_game)
            win = move.check_for_victory()
            if win:
                current_game.won = request.user
                current_game.save()
            else:
                move.change_current_player()
            d = move_serializer.data
            d['win'] = win
            return Response(d, status=status.HTTP_201_CREATED)
        return Response(move_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def get_moves(self, request, pk):
        serializer = MoveSerializer(Move.objects.filter(game_id=pk), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HighScoreView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = get_user_model().objects.annotate(won=Count('won_games')).order_by('-won')
    serializer_class = HighScoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MoveViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
