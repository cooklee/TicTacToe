import random

from django.conf import settings
from django.db import models
from django.db.models import Q

from tictactoe_game.board import check_if_win, Point


class Game(models.Model):
    name = models.CharField(max_length=31, default="")
    board_size = models.IntegerField(default=3)
    line_length = models.IntegerField(default=3)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    won = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.SET_DEFAULT,
                            related_name="won_games")
    current_player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       related_name='waiting_games', blank=True, null=True)

    class Meta:
        ordering = ('id',)

    def set_current_player(self):
        self.current_player = random.sample(set(self.players.all()), 1)[0]
        self.save()

    @property
    def is_active(self):
        return self.won is None

    def __str__(self):
        return f"{self.id} active {self.is_active} size {self.board_size}"


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['x', 'y', 'game'], name='only_one_move_per_game')
        ]
        ordering = ('game__id',)

    def check_for_victory(self):
        all_moves = self.game.move_set.filter(user=self.user)
        board = self._create_board(all_moves)
        return check_if_win(board, Point(self.x, self.y), self.game.line_length)

    def _create_board(self, moves):
        size = self.game.board_size
        board = [[0 for x in range(size)] for y in range(size)]
        for move in moves:
            board[move.x][move.y] = 1
        return board

    def change_current_player(self):
        self.game.current_player = self.game.players.get(~Q(id=self.game.current_player.id))
        self.game.save()

    def __str__(self):
        return f"({self.x} {self.y}) {self.user} {self.game.id}"