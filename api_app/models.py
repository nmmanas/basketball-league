from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Coach(BaseModel):
    coach_name = models.CharField(max_length=100)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Coaches"

    def __str__(self):
        return self.coach_name

class Team(BaseModel):
    team_name = models.CharField(max_length=100)
    average_score = models.FloatField()
    coach = models.OneToOneField(Coach, related_name='team', default=0, on_delete=models.PROTECT)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.team_name

class Player(BaseModel):
    player_name = models.CharField(max_length=100)
    player_height = models.FloatField()
    average_score = models.FloatField()
    no_of_games = models.IntegerField()
    team = models.ForeignKey(Team, related_name='players', default=0, on_delete=models.PROTECT)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Players"

    def __str__(self):
        return self.player_name

class Tournament(BaseModel):
    tournament_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    rounds = models.IntegerField()

    class Meta:
        verbose_name_plural = "Tournaments"

    def __str__(self):
        return self.tournament_name

class Game(BaseModel):
    tournament = models.ForeignKey(Tournament, related_name='games', on_delete=models.PROTECT)
    game_date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_team', default=None, blank=True, null=True, on_delete=models.PROTECT)
    away_team = models.ForeignKey(Team, related_name='away_team', default=None, blank=True, null=True, on_delete=models.PROTECT)
    home_team_score = models.FloatField(default=0)
    away_team_score = models.FloatField(default=0)
    home_team_from_game = models.ForeignKey('self', related_name='home_team_game', default=None, blank=True, null=True, on_delete=models.PROTECT)
    away_team_from_game = models.ForeignKey('self', related_name='away_team_game', default=None, blank=True, null=True, on_delete=models.PROTECT)
    winner = models.ForeignKey(Team, related_name='winner', default=None, blank=True, null=True, on_delete=models.PROTECT)
    round_number = models.IntegerField()

    # rounds will be:
    # 1 - Round 1
    # 2 - Quarter Finals
    # 3 - Semi Finals
    # 4 - Final

    class Meta:
        verbose_name_plural = "Games"

    def __str__(self):
        return f'{self.tournament.tournament_name} | Round {self.round_number} | {self.game_date}'

class UserLoginActivity(models.Model):
    login_username = models.CharField(max_length=40, null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    logout_datetime = models.DateTimeField(default=None, null=True, blank=True)


