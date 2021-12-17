from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def score(self):
        return self.won_games.count()
