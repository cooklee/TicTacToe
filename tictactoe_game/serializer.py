from rest_framework import serializers

from tictactoe_game.models import Game, Move


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['board_size', 'line_length', 'players', ]

def even_number(value):
    if value <= 0:
        raise serializers.ValidationError('This field has to be bigger then 0')

class MoveSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Move
        fields = ['id', 'x', 'y', 'game', 'user']

    def validate_x(self, value):
        if value < 0 :
            raise serializers.ValidationError('Rating has to be between 1 and 10.')
        return value

