from django.db.models import Count
from rest_framework import serializers
from django.contrib.auth import get_user_model
from tictactoe_game.models import Game, Move


class GameSerializer(serializers.ModelSerializer):
    current_player = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'board_size', 'line_length', 'players', 'current_player']


class MoveSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Move
        fields = ['id', 'x', 'y', 'user']

    #
    def _get_game(self):
        game_id = self.context.get("view").kwargs.get('pk')
        self.game = Game.objects.get(pk=game_id)
        return self.game

    def _check_if_in_range(self, value):
        game = self._get_game()
        if value < 0 or value > game.board_size:
            raise serializers.ValidationError(f'value have to be between 1 and {game.board_size}')

    def validate_x(self, value):
        self._check_if_in_range(value)
        return value

    def validate_y(self, value):
        self._check_if_in_range(value)
        return value

    def validate(self, attrs):
        x, y, user = attrs['x'], attrs['y'], self.context['request'].user
        if not self.game.is_active:
            raise serializers.ValidationError('This game is over')
        if user != self.game.current_player:
            raise serializers.ValidationError("its not your move")
        try:
            Move.objects.get(game=self.game, x=x, y=y)
            raise serializers.ValidationError(f"field {x},{y} already taken")
        except Move.DoesNotExist:
            return super().validate(attrs)

class HighScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'score']
